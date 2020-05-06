"""
    Resolucion de Ecuacion Cuadratica Poblacional
    
    Autor: Julian Ariel Campana
"""
from sympy import *

#Definimos los simbolos a utilizar en nuestra ecuacion diferencial
t = symbols("t")
alpha = symbols('alpha')
beta = symbols('beta')
C1, p_0 = symbols('C1 p_0')
r, K = symbols('r K')

f = Function('f')

resultado = f(t)

dfdt = diff(f(t), t)

# d/dt f(t) = alpha . f(t) + beta . f(t)^2 (Ecuación)

eq_diff = Eq(dfdt, alpha*f(t) + beta*f(t)**2)
print("\nEcuacion cuadratica:")
print(eq_diff)

solucion_eq = dsolve(eq_diff)
print("\nSolucion general:")
print(solucion_eq)

# f(0) = p_0

particular = solucion_eq.subs(C1, p_0)
print("\nSolucion particular:")
print(particular)

"""
Resolucion de la ecuacion cuadratica 
reemplazando alpha y beta por r y K
    r = alpha
    K = - alpha / beta
""" 
eq_diff2 = Eq(diff(f(t), t) , r * (1-f(t)/K) * f(t))
print(eq_diff2)

print("\nSolucion general:")
solucion_eq = dsolve(eq_diff2)
print(solucion_eq)

print("\nSolucion general de la parte derecha:")
general = solucion_eq.rhs
print(general)

print("\nSolucion general de la parte derecha con t = 0:")
general_t0 = general.subs(t, 0)
print(general_t0)

print("\nCondicion Inicial:")
condicion_inicial = Eq(general_t0, p_0)
print(condicion_inicial)

print("\nSe calcula la solucion para resolver C1:")
solucion = solve(condicion_inicial, C1)
print(solucion[0])

valor_C1 = solucion[0]

print("\nResultado final:")
particular = general.subs(C1, valor_C1)
print(particular)

print("\nSimplificación del resultado final:")
particular_simple = simplify(particular)
print(particular_simple)

print("\nSe verifica que el resultado final sea correcto:")
print(particular_simple.subs(t, 0))
