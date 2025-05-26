import random

def count_sequences(seq, l):
    target = 'C' * l
    return target in ''.join(seq)

def empiric(nr_aruncari, l, nr_sim=10000):
    cnt = 0
    for _ in range(nr_sim):
        seq = [random.choice(['C', 'P']) for _ in range(nr_aruncari)]
        if count_sequences(seq, l):
            cnt+=1
    return cnt / nr_sim


n = 4 #pt 10 aruncari
print(f"P empirica pentru trei C cu {n} aruncari: {empiric(n, 3) :.4f}")
print(f"P empirica pentru patru C cu {n} aruncari: {empiric(n, 4) :.4f}")
