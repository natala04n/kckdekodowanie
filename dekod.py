import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv('sygnal.csv', delimiter=',', engine='python', names=['k1', 'k2', 'k3', 'k4', 'k5', 'k6'])

t = np.linspace (0, 37.86, 200*37.86)
sygnal=dane['k2']
plt.plot(t, sygnal)
plt.title('Zebrany sygnał')
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

liczby = dane['k6']

filtrowanie1 = ag.pasmowozaporowy(sygnal, 200, 49, 51)
filtrowanie2 = ag.gornoprzepustowy(filtrowanie1, 200, 3)
plt.plot(t,filtrowanie2)
plt.title('Zebrany sygnał po filtracji')
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

for i in range(len(filtrowanie2)):
    if filtrowanie2[i]>0.15:
        print(liczby[i],i)
        
