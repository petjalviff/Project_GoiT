import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Визначення символьних змінних
x = sp.Symbol('x')
pi=np.pi
# print("pi=",pi)
e=np.exp(1)
# print("e=",e)

# Визначення функції
f=2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))

# Обчислення невизначеного інтегралу
indefinite_integral = sp.integrate(f, x)

# Виведення невизначеного інтегралу
print("Невизначений інтеграл:", indefinite_integral)

# Обчислення інтегралу від a до b
a = 9
b = 18
definite_integral = sp.integrate(f, (x, a, b))

# Виведення інтегралу від a до b
print("Інтеграл від {} до {}: {}".format(a, b, definite_integral))

# Визначення точок для графіку
x_values = np.linspace(0, 24, 100)
y_values = np.array([f.subs(x, val) for val in x_values])

# Побудова графіку функції
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label='f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік функції sin(x)')
plt.grid(True)
plt.legend()
plt.show()
