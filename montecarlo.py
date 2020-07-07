import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import itertools as it
import random

datos = [6,6,7,9,10,10,11,11,11,11,11,12,12,12,13,13,14,14,14,14,14,15,15,15,15,15,16,16,16,16,16,16,16,
16,16,16,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,
19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,21,21,21,21,21,22,22,22,
22,22,22,22,22,22,22,22,22,22,22,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,
24,24,24,24,24,24,24,24,24,24,24,25,25,25,25,25,25,25,25,25,25,25,25,25,26,26,26,26,26,26,26,26,
26,26,27,27,27,27,27,27,27,27,27,28,28,28,28,28,28,29,29,29,29,29,29,29,29,30,30,30,30,30,30,30,
30,30,30,30,31,31,31,31,31,31,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,33,33,33,33,33,33,34,
34,34,34,35,35,35,35,35,36,36,36,37,37,37,37,37,38,38,39,39,40,42,43,44,46]

array = np.array(datos)

r = []
data_montecarlo = []

# Calculo de la media
def media(array):
    return np.mean(array)

# Calculo de la varianza
def var(array):
    return np.var(array)

# Calculo de la desviación estandar
def desv_est(array):
    return np.std(array)

# Calculo del máximo
def max(array):
    return np.max(array)

# Calculo del mínimo
def min(array):
    return np.min(array)

# Intervalos de 6 a 46
x = np.arange(min(array), max(array)+1)

print("Medidas Estadisticas para los datos historicos \n")

print("Media: ", media(array))
print("Varianza: ", var(array))
print("Desviacion estándar: ", desv_est(array))
print("Maximo: ", max(array))
print("Minimo: ", min(array))

# Distribución normal
dn = ss.norm.pdf(x, loc=media(array), scale=desv_est(array))
plt.plot(x, dn)
plt.title('Distribución Normal')
plt.ylabel('probabilidad de los valores de la distribucion normal')
plt.xlabel('datos')
plt.savefig('distribucion-normal.jpg')

# Distribución acumulada
da = list(it.accumulate(dn))
plt.clf()
plt.plot(x, da)
plt.title('Distribución Acumulada')
plt.ylabel('probabilidad')
plt.xlabel('datos')
plt.savefig('distribucion-acumulada.jpg')

#Se comparan los valores aleatorios con la acumulada

# Montecarlo

for i in range(100):
    r.append(random.uniform(0, 1))

plt.clf()
plt.plot(r)
plt.title('Randoms')
plt.xlabel('Valores Aleatorios')
plt.ylabel('Distribucion Acumulada')

plt.savefig('randoms.jpg')

for i in range(0, 99):
    for j in range(1, 40):
        if r[i] <= da[0]:
            data_montecarlo.append(x[j])
                
        elif da[j-1] < r[i] < da[j]:
            data_montecarlo.append(x[j])       

print("\n \n Datos Generados \n")
print(data_montecarlo)
print("\n")

plt.clf()
plt.plot(da)
plt.title('Visitas')
plt.xlabel('Distribucion Acumulada')
plt.ylabel('Cantidad de Valores de los Intervalos')
plt.savefig('visitas.jpg')

print("Medidas Estadisticas para los datos generados \n")

print("Media: ", media(data_montecarlo))
print("Varianza: ", var(data_montecarlo))
print("Desviacion estándar: ", desv_est(data_montecarlo))
print("Maximo: ", max(data_montecarlo))
print("Minimo: ", min(data_montecarlo))
