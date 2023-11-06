import random
import itertools
import numpy as np

player = 0.5
games = 15
min_round = 0
points = 0
spiel_list = [x for x in range(1, games + 1)]
half = sum(spiel_list) / 2
for x in range(1, games + 1):
    min_round += 1
    points += x
    if points > half:
        break
print('Mindestanzahl an zu spielenden Games {}'.format(min_round))
var_games = itertools.product(range(2), repeat=15)
var_games = [x for x in var_games]  # Alle möglichen Konstellationen der Runden
draw_p = 0
num_rounds = [0 for x in range(0, games)]
for x in range(0, len(var_games)):
    var_p = np.dot(var_games[x], spiel_list)  # Punktestand in der Konstellation
    if var_p == half:
        draw_p += 1  # Anzahl an Unentschieden
    p_round = 0
    for i, v in enumerate(var_games[x]):
        if v == 1:  # Spiel gewonnen
            p_round += v * (i + 1)  # Punktestand nach jeder Runde
        if p_round == half and i == len(spiel_list)-1: # bei Gewinn oder Unentschieden bei Ende des Spiels
            num_rounds[i] += 1
            break
        if p_round > half: # bei Gewinn vor Ende
            num_rounds[i] += 2
            break

print('Anzahl der möglichen Unentschieden {}'.format(draw_p))
print('Wahrscheinlichkeit auf Unentschieden {:.2f}'.format((draw_p / len(var_games)) * 100))
print('Wahrscheinlichkeiten der Spielrunden {}'.format([x / sum(num_rounds) * 100 for x in num_rounds]))
#print(sum(num_rounds)) # berücksichtigte Fälle

win_rounds = [0 for x in range(0, games)]
shows = 1000000
for show in range(1, shows+1):
    p = [0, 0] # Punktestand
    for spiel in range(1, games+1):
        p[random.randint(0, 1)] += spiel
        if p[0] > half or p[1] > half:
            break
    win_rounds[spiel-1] += 1
print('Wahrscheinlichenkeiten der Spielrunden bei gleichstarken Gegnern {}'.format([x / shows * 100 for x in win_rounds]))



