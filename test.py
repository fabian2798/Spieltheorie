import itertools
import numpy as np

games = [x for x in range(1,16)]
var_games = itertools.product(range(2), repeat=15)
var_games = [x for x in var_games]
var_2 = np.dot(var_games[3], games)
temp = 0
full = sum(games)
punkte = 0
ind = 0
for i, v in enumerate(var_games[3]):
    punkte += v*(i+1)
    full -= v*(i+1)
    ind += 1
print(var_games[3])
print(var_2)
print(punkte)
print(full)
print(ind)
"""
def win_afterround(shows):
    win_p1 = []
    win_p2 = []
    draw = 0
    run = 1
    while run <= shows:
        p = [0, 0]  # Punktestand
        for spiel in range(1, games + 1):
            p[random.randint(0, 1)] += spiel
            if p[0] > half :
                win_p1.append(spiel)
                break
            elif p[1] > half:
                win_p2.append(spiel)
                break
        if p[0] == p[1]:
            draw += 1
        run += 1
    return draw, win_p1, win_p2
"""
# if p_round - temp == 0 and i < len(spiel_list) - 1:  # unentschieden und spiel noch nicht vorbei
# continue
# if p_round - temp == 0 and i == len(spiel_list) - 1:  # unentschieden in letzter Runde
# num_rounds[i] += 1  # Spieler A oder B
# break
# else:
# num_rounds[i] += 2  # Spieler A und B
# break
temp = sum(spiel_list)
temp -= v + (i * 1)  # Noch mögliche Punkte