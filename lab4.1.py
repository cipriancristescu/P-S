import random

def monty_hall(s=100000):
    win_change = 0
    win_keep = 0
    for _ in range(s):
        d= ['c', 'c', 'm']
        random.shuffle(d)

        chosen_door = random.randint(0, 2)
        revealed_door = random.choice([i for i in range(3) if i != chosen_door and d[i] == 'c'])

        if d[chosen_door] == 'm':
            win_keep += 1
        else:
            win_change += 1

    print(f"castig daca schimbi: {win_change / s:.2f}")
    print(f"castig daca pastrezi: {win_keep / s:.2f}")


monty_hall()
