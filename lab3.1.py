import numpy as np
import matplotlib.pyplot as plt
import time

# moneda echilibrata
def ban(aruncari):
    cap = 0
    raport_cp = []

    for i in range(1, aruncari + 1):
        x= np.random.random()
        if x < 0.5:
            cap+= 1
        raport_cp.append(cap / i)

    return cap, raport_cp
def ban1(aruncari):
    l=np.random.random(aruncari)
    l=l<0.5
    cap1=np.sum(l)
    l=np.cumsum(l)
    index=np.arange(1,aruncari+1)
    l=np.divide(l,index)
    return cap1,l
aruncari = 10**6
tic=time.perf_counter()
cap, raport_cp = ban(aruncari)
print(f"Din {aruncari} aruncari, moneda echilibrată a căzut de {cap} ori pe cap.")
toc=time.perf_counter()
print(toc-tic)

tic=time.perf_counter()
cap1,raport_cp1=ban1(aruncari)
toc=time.perf_counter()
print(f"Din {aruncari} aruncari, moneda echilibrata a căzut de {cap1} ori pe cap.")
print(toc-tic)



plt.plot(range(1, aruncari + 1), raport_cp)
plt.axhline(y=0.5, color='r')
plt.title('Proportia de capete în functie de nr de aruncari')
plt.xlabel('Aruncari')
plt.ylabel('Cap')
plt.show()


plt.plot(range(1, aruncari + 1), raport_cp1)
plt.axhline(y=0.5, color='r')
plt.title('Proportia de capete în functie de nr de aruncari')
plt.xlabel('Aruncari')
plt.ylabel('Cap')
plt.show()