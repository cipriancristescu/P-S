# moneda masluita
import numpy as np
import matplotlib.pyplot as plt

def ban_m(aruncari):
    cap = 0
    raport_cp= []

    for i in range(1, aruncari + 1):
        x= np.random.random()
        if x < 0.75:
            cap += 1
        raport_cp.append(cap / i)

    return cap, raport_cp

aruncari=10000
cap, raport_cp = ban_m(aruncari)
print(f"Din {aruncari} aruncari, moneda a cazut de {cap} ori pe cap.")


plt.plot(range(1, aruncari + 1), raport_cp)
plt.axhline(y=0.5, color='r')
plt.title('Proportia de capete în functie de nr de aruncari')
plt.xlabel('Aruncari')
plt.ylabel('Cap')
plt.show()
