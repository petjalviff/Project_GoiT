import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad
# Визначення символьних змінних
x = sp.Symbol('x')
pi=np.pi
# print("pi=",pi)
e=np.exp(1)
# print("e=",e)

# Визначення функції
f=2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))

# Обчислення невизначеного інтегралу
# indefinite_integral = sp.integrate(f, x) # - Невизначений інтеграл

# Виведення невизначеного інтегралу
# print("Невизначений інтеграл:", indefinite_integral)

# Обчислення інтегралу від a до b
a = 9
b = 18
# definite_integral = sp.integrate(f, (x, a, b))

# Виведення інтегралу від a до b
# print("Інтеграл від {} до {}: {}".format(a, b, definite_integral))

# Визначення точок для графіку
# x_values = np.linspace(0, 24, 100)
# y_values = np.array([f.subs(x, val) for val in x_values])

# # Побудова графіку функції
# plt.figure(figsize=(10, 5))
# plt.plot(x_values, y_values, label='f(x) = sin(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Графік функції sin(x)')
# plt.grid(True)
# plt.legend()
# plt.show()



# *********************<<<<<<< Homework 6.2 >>>>>>>>>>****************
#Функція для чисельного інтегрування методом прямокутників

# def rectangle_integrate(func, a,b,n):
#     x_f=np.linspace(a,b,n+1) #генерування n рівномірно розподілених точок
#     # print (x_f)
#     delta_x=(b-a)/n # визначення ширини кожного прямокутника
#     integral=np.sum(func(x_f[:-1])*delta_x) #обчислення суми площ всіх прямокутників
#     return integral

# def function(x): #Функція що задається для обчислення (із ДЗ)
#     pi=np.pi
#     e=np.exp(1)
#     return 2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))  # Приклад функції, яку потрібно інтегрувати

# a1 = 9
# b1 = 18
# n1=9

# print(rectangle_integrate(function,a1,b1,n1))

# *********************<<<<<<< Homework 6.3 >>>>>>>>>>****************
#Функція для чисельного інтегрування методом трапецій

# def trapeze_integrate(func, a,b,n):
#     x_f=np.linspace(a,b,n+1) #генерування n рівномірно розподілених точок
#     delta_x=(b-a)/n # визначення ширини кожної трапеції
#     y_f = func(x_f)  # Значення функції на цих точках
#     integral = delta_x*(np.sum(y_f)-0.5*(y_f[0]+y_f[-1]))  # Формула визначення інтегралу методом трапецій
#     return integral

# def function(x): #Функція що задається для обчислення (із ДЗ)
#     pi=np.pi
#     e=np.exp(1)
#     return 2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))  # Приклад функції, яку потрібно інтегрувати

# a1 = 9
# b1 = 18
# n1=50

# print(trapeze_integrate(function,a1,b1,n1))


# *********************<<<<<<< Homework 6.4 >>>>>>>>>>****************
#Функція для чисельного інтегрування методом Сімпсона

# def simpson_integrate(func, a,b,n): #Обов'язкова умова n - має бути парним числом!
#     x_f=np.linspace(a,b,n+1) #генерування n рівномірно розподілених точок
#     delta_x=(b-a)/n # визначення ширини
#     integral = delta_x / 3 * (func(x_f)[0] + 4 * np.sum(func(x_f)[1:-1:2]) + 2 * np.sum(func(x_f)[2:-1:2]) + func(x_f)[-1])  # Формула визначення інтегралу методом Сімпсона
#     return integral

# def function(x): #Функція що задається для обчислення (із ДЗ)
#     pi=np.pi
#     e=np.exp(1)
#     return 2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))  # Приклад функції, яку потрібно інтегрувати

# a1 = 9
# b1 = 18
# n1=50

# print("Інтеграл від a до b рівний -", simpson_integrate(function,a1,b1,n1))


# *********************<<<<<<< Homework 6.5 >>>>>>>>>>****************
'''Обчислення інтегралу з допомогою функції scipy.integrate.quad'''

def function(x): #Функція що задається для обчислення (із ДЗ)
    pi=np.pi
    e=np.exp(1)
    return 2*((4/(1.2*np.sqrt(2*pi)))*e**((-1/2)*((x-11)/1.2)**2)+(7/(2.4*np.sqrt(2*pi)))*e**((-1/2)*((x-15)/2.4)**2))  # Приклад функції, яку потрібно інтегрувати

a1 = 9
b1 = 18

integral_q = quad(function, a1, b1)

print("Значення інтегралу:", integral_q)
# print("Похибка оцінки:", error_q)
# print("Інтеграл від a до b рівний -", simpson_integrate(function,a1,b1,n1))