# import sympy as sp

# # Створення символьної змінної x
# x=sp.symbols("x")
# print("")
# print("Визначення функції №1")
# # Визначення функції
# f=(x**3)/3+(x**2)/2-2*x


# # Обчислення похідної функції
# dx=sp.diff(f,x)

# # Вивід похідної функції
# print("-->Похідна функції f:", dx)

# # Обчислення значень похідних у точках x=1 і x=-1/2
# x_f = [1, -1/2]
# for value in x_f:
#     derivative_function=dx.subs(x, value)
#     print(f"-->Значення похідної у точці x={value}: {derivative_function}")

# print("")
# print("Визначення функції №2")
# f2=(x**2+1)**(1/2)
# dx2=sp.diff(f2,x)
# print("-->Похідна функції f2:", dx2)
# for i in x_f:
#     derivative_function=dx2.subs(x,i)
#     print(f"-->Значення похідної у точці x={i}: {derivative_function}")

# print("")
# print("Визначення функції №3")
# f3=1/((x**2+1)**(1/2))
# dx3=sp.diff(f3,x)
# print("-->Похідна функції f3:", dx3)
# for i in x_f:
#     derivative_function=dx3.subs(x,i)
#     print(f"-->Значення похідної у точці x={i}: {derivative_function}")


import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def f_y(x):
    return -3 * x**2 + 30 * x

# Визначення похідної функції
def f_derivative(x):
    return -6*x+30

# Генерація значень x в інтервалі [-5, 10]
x_i = np.linspace(-5, 10, 20)
# Обчислення відповідних значень y
y_i = f_y(x_i)

# Обчислення значень похідної для знаходження точки максимуму
critical_point = 5
max_point = (critical_point, f_y(critical_point))

# Вивід графіків
plt.figure(figsize=(10, 6))
plt.plot(x_i, y_i, label='Функція y=-3x^2+30x')
plt.plot(x_i, f_derivative(x_i), label='Похідна функції')
plt.scatter(max_point[0], max_point[1], color='orange', label='Точка максимуму')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції та її похідної')
plt.legend()
plt.grid(True)
plt.show()
