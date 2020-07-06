import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


np.seterr(divide='ignore', invalid='ignore')

# Parámetros
r1 = 0.1
p = 0.02
r2 = 0.3
a = 0.01
r = 0.001

# Condiciones iniciales

liebres = 500    # Presas
zorros = 10  # Depredadores

conds_iniciales = np.array([liebres, zorros])

# Condiciones para integración
tf = 500
n = 2000
t = np.linspace(0, tf, n)

def df_dt(x, t, r1, p, r2, a):
    dx = r1 * x[0] - p * x[0] * x[1]
    dy = -r2 * x[1] + a * x[0] * x[1]
    return np.array([dx, dy])

def df_dt_logistic(x, t, r1, p, r2, a, r):
    dx = r1 * x[0] - r * x[0] ** 2 - p * x[0] * x[1]
    dy = - r2 * x[1] + a * x[0] * x[1]
    return np.array([dx, dy])

def c(x, r1, p, r2, a):
    return r1 * np.log(x[1]) - p * x[1] + r2 * np.log(x[0]) - a * x[0]

solucion = odeint(df_dt, conds_iniciales, t, args=(r1, p, r2, a))

solucion_logistica = odeint(df_dt_logistic, conds_iniciales, t, args=(r1, p, r2, a, r))

n_max = np.max(solucion) * 1.10

x_max = np.max(solucion_logistica[:, 0]) * 1.05
y_max = np.max(solucion_logistica[:, 1]) * 1.05

x = np.linspace(0, x_max, 25)
y = np.linspace(0, y_max, 25)

xx, yy = np.meshgrid(x, y)
uu, vv = df_dt_logistic((xx, yy), 0, r1, p, r2, a, r)
norm = np.sqrt(uu**2 + vv**2)
uu = uu / norm
vv = vv / norm

plt.clf()
plt.plot(t, solucion_logistica[:, 0], 'r-', label='presa')
plt.plot(t, solucion_logistica[:, 1], 'b-', label='depredador')
plt.legend()
plt.xlabel('Tiempo (Semanas)', fontsize=12)
plt.ylabel('Poblaciones', fontsize=12)

plt.savefig('grafico_de_elongacion.png')

plt.clf()
plt.quiver(xx, yy, uu, vv, norm, cmap=plt.cm.gray)
plt.plot(solucion_logistica[:, 0], solucion_logistica[:, 1], lw=2, alpha=0.8)
plt.xlabel('Presa', fontsize=12)
plt.ylabel('Predador', fontsize=12)
plt.savefig('grafico_de_fase.png')

x = np.linspace(0, x_max, 100)
y = np.linspace(0, y_max, 100)
xx, yy = np.meshgrid(x, y)
constant = c((xx, yy), r1, p, r2, a)

plt.figure('distintas_soluciones', figsize=(8,5))
plt.contour(xx, yy, constant, 50, cmap=plt.cm.Blues)
plt.xlabel('Presas')
plt.ylabel('Predadores')
plt.savefig('grafico_punto_de_estabilidad.png')
