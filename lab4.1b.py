import random

def monty_hall_n(n, s=100000):
    win_change = 0
    win_keep = 0

    for _ in range(s):
        d= ['c'] * (n - 1) + ['m']
        random.shuffle(d)

        chosen_door = random.randint(0, n - 1)
        revealed_doors = random.sample([i for i in range(n) if i != chosen_door and d[i] == 'c'], n - 2)

        if d[chosen_door] == 'm':
            win_keep += 1
        else:
            win_change += 1

    print(f"Pentru {n} usi:")
    print(f"P daca schimbi: {win_change / s:.2f}")
    print(f"P daca pastrezi: {win_keep / s:.2f}")


monty_hall_n(4)
monty_hall_n(5)
monty_hall_n(10)
