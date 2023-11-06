import random
import matplotlib.pyplot as plt

# Berechnung der Anzahl der unentschiedenen Spielrunden
# erzeugt List [1,2,0,4,0,6,....15] mit gewonnen Spielrunden für eine bestimmte Zahl i
def convertBin(i,x):    # x sind die Spielrunden
    #print(i,x)
    s = ''.join(bin(i).split('0b')) # erzeugt binärdarstellung der gewonnen Spiele (110101....1)
    l1 = list(s.zfill(x))   # binäre Gewinnliste
    l2 = range(1,x+1)   # mögliche Punkte in den Spielrunden
    #print(list(map(lambda x,y: int(x)*int(y),l1,l2)))
    return list(map(lambda x,y: int(x)*int(y),l1,l2))   # Mit Punkten gewichtete Gewinnliste


rounds=15    # Anzahl Spielrunden
half = sum(range(1, rounds + 1)) / 2   # halbe Summe von allen Spielrunden
minRounds = 0
tsum= 0
p = [0 for i in range(0, rounds)]
for i in range(1,rounds+1): # geht aber auch analytisch zu berechnen (quadrat. Gl.)
    minRounds += 1
    tsum += i
    if tsum > half:
        break

print("Minimale Rundenanzahl: {}".format(minRounds))
drawn = 0   # Anzahl der Unentschieden
for i in range(0, 2 ** rounds ): # z.B. i= 0..2**3-1 Anzahl 000, 001, 010, 011, 100, 101, 110, 111
    permList = convertBin(i, rounds)  # Umwandlung in Liste mit Spielrunden [0,0,0] [0,0,3] [0,2,0]
    summe = sum(permList)         # Summe bilden
    if summe == half:             # Falls genau die hälfte...
        drawn +=1                 # zählen als unentschieden

    # Berechnung der exakten Wahrscheinlichkeiten für die Rundenanzahl
    points = 0
    rest = 2 * half               # noch verfügbare Punkte
    for r,i in enumerate(permList):
        points += i               # Summe Spieler A
        rest -= i                 # Noch verfügbar
        if  points-rest >= 0:     # Spiel zuende
            if points - rest == 0 and r < len(permList) - 1:  # bisher unentschieden, weitergucken
                continue
            if points - rest == 0 and r == len(permList) - 1: # unentschieden in letzter Runde
                p[r] += 1  # Spieler A oder B
                break
            else:
                p[r] += 2           # Spieler A und B
                break
print(p)
print("Wahrscheinlichkeiten : {}".format([i/(2**rounds)*100 for i in p]))
print("Anzahl: {:4d} Wahrscheinlichkeit:{:5.2f}%".format(drawn, drawn / 2 ** rounds * 100))


# Simulation zur Berechnung der Wahrscheinlichkeiten der maximalen Spielrunden
simmax = 10000 # Anzahl der Simulationen
print("SIMULATION")
# p enthält Häufigkeiten der Spielrunden (mit 0 initialisieren) (<rounds> Plätze)
p0 = [0 for i in range(0, rounds)]
p1 = [0 for i in range(0, rounds)]
p2 = [0 for i in range(0, rounds)]
for sim in range(1,simmax+1):
    rest = sum(range(1,rounds+1))   # Summe der noch erreichbaren Punkte
    s0 = [0, 0]                     # Spielstand initialisieren
    # Spiele durchführen
    for game in range(1, rounds + 1):
        s0[random.randint(0, 1)] += game    # Gegner sind gleich stark
        rest -= game
        # Abbruch falls nicht mehr schlagbar
        if abs(s0[0] - s0[1]) > rest:   # Runde zum Unentschieden zulassen (andernfalls >=)
            break
    p0[game - 1] += 1                   # Häufigkeiten mitzählen (p ist zero based)
    rest = sum(range(1,rounds+1))       # Summe der noch erreichbaren Punkte
    s0 = [0, 0]      # Spielstand initialisieren
    for game in range(1, rounds + 1):
        # Gegner sind unterschiedlich stark (1:2)
        x=2
        rn = random.randint(0,x)
        if rn==x:
            s0[1] +=game
        else:
            s0[0] += game

        rest -= game
        # Abbruch falls nicht mehr schlagbar
        if abs(s0[0] - s0[1]) > rest:   # Runde zum Unentschieden zulassen (andernfalls >=)
            break
    p1[game - 1] += 1                   # Häufigkeiten mitzählen (p ist zero based)
    rest = sum(range(1,rounds+1))   # Summe der noch erreichbaren Punkte
    s0 = [0, 0]      # Spielstand initialisieren
    for game in range(1, rounds + 1):
        # Gegner sind unterschiedlich stark (1:3)
        x=3
        rn = random.randint(0,x)
        if rn==x:
            s0[1] +=game
        else:
            s0[0] += game

        rest -= game
        # Abbruch falls nicht mehr schlagbar
        if abs(s0[0] - s0[1]) > rest: # Runde zum Unentschieden zulassen (andernfalls >=)
            break
    p2[game - 1] += 1  # Häufigkeiten mitzählen (p ist zero based)

print("Anzahl der simulierten Spielturniere: {}".format(simmax))
print("(1:1) Wahrscheinlichkeiten ab {}. Spielrunde: {}".
      format(minRounds,['{:4.1f}'.format(i / simmax * 100) for i in p0[minRounds-1:]]))
print("(1:2) Wahrscheinlichkeiten ab {}. Spielrunde: {}".
      format(minRounds,['{:4.1f}'.format(i / simmax * 100) for i in p1[minRounds-1:]]))
print("(1:3) Wahrscheinlichkeiten ab {}. Spielrunde: {}".
      format(minRounds,['{:4.1f}'.format(i / simmax * 100) for i in p2[minRounds-1:]]))

# Grafische Darstellung
plt.subplot(311)
index = range(1, rounds + 1)  # 1,...,15
val = [i / simmax * 100 for i in p0]  # Prozentuale Häufigkeiten
plt.bar(index, val, 0.8)
for i in range(len(val)):
    if val[i] != 0:
        plt.annotate("{:3.1f}".format(val[i]), (0.5 + i, val[i] + 1))
plt.title("Schlag den Star, Wahrscheinlichkeit der Runden \n(bei {} Simulationen)".format(simmax))
plt.ylabel("P in %")
axes = plt.gca()
axes.set_ylim([None, 100])
plt.xticks(index, index)  # labels get centered
plt.annotate("Anzahl der Unentschieden: {:4d},  ({:<.1f}% der Spiele)".
             format(drawn, drawn / 2 ** rounds * 100), xy=(1, 90))
plt.annotate("Spielerstärken: 1:1", xy=(1, 80))
plt.subplot(312)
index = range(1, rounds + 1)  # 1,...,15
val = [i / simmax * 100 for i in p1]  # Prozentuale Häufigkeiten

plt.bar(index, val, 0.8)
for i in range(len(val)):
    if val[i] != 0:
        plt.annotate("{:3.1f}".format(val[i]), (0.5 + i, val[i] + 1))
plt.ylabel("P in %")
axes = plt.gca()
axes.set_ylim([None, 100])
plt.xticks(index, index)  # labels get centered
plt.annotate("Spielerstärken: 1:2", xy=(1, 80))
plt.subplot(313)
index = range(1, rounds + 1)  # 1,...,15
val = [i / simmax * 100 for i in p2]  # Prozentuale Häufigkeiten

plt.bar(index, val, 0.8)
for i in range(len(val)):
    if val[i] != 0:
        plt.annotate("{:3.1f}".format(val[i]), (0.5 + i, val[i] + 1))
plt.xlabel("Spielnummer")
plt.ylabel("P in %")
axes = plt.gca()
axes.set_ylim([None, 100])
plt.xticks(index, index)  # labels get centered
plt.annotate("Spielerstärken: 1:3", xy=(1, 80))
plt.show()