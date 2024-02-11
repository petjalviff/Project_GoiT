# Створення та виклик функції
# c=39 #my age
# def hello_en():
#     print("Hello world")
#     print("What is your name?")
#     a=input("Enter your name: ")
#     print(f"Hello {a}, how old you?")
#     b=int(input("Enter years old: "))
#     try:
#         if b<c:
#             d=c-b
#             print(f"I am {d} years older than you, {a}" )
#         else:
#             if b==c:
#                 print("We are the same age as you")
#             else: d=b-c
#             print(f"I am {d} years younger than you, {a}")
    
#     except ValueError:
#         print("You enterned not Integer!")
#         b=int(input("Enter years old: "))
#     except IndentationError:
#         print("You enterned not Integer!")
#         b=int(input("Enter years old: "))
# def hello_ua():
#     print("****************")
#     print("Привіт")
#     print("Як тебе звати?")
#     a=input("Введи своє імя: ")
#     print(f"Привіт, {a}, скільки тобі років?")
#     b=int(input("Введи свій вік: "))
#     try:
#         if b<c:
#             d=c-b
#             print(f"Я на {d} роки(ів) старший від тебе, {a}" )
#         else:
#             if b==c:
#                 print("Ми з тобою одного віку")
#             else: d=b-c
#             print(f"я на {d} роки(ів) молодший, {a}")
    
#     except ValueError:
#         print("You enterned not Integer!")
#         b=int(input("Enter years old: "))
#     except IndentationError:
#         print("You enterned not Integer!")
#         b=int(input("Enter years old: "))
# while True:
#     leng=input("Enter lenguage (en for English or ua for Ucrainian): ")
#     if leng=="ua":
#         hello_ua()
#     else: hello_en()
#     print("Godbye")
#     print("*******************")



# Зміння кількість параметрів
# def total(a=6, *pbook, **car):
#     a=1
#     print("a =",a)
#     # прохід по всіх елементах кортежу
#     for sitem in pbook:
#         print('single_item', sitem)

#     #прохід по всіх елементах словника
#     for f_part, s_part in car.items():
#         print(f_part,":",s_part)

# print(total(5, 1, {6}, "a", 5, 2, 3, {"Jack":55555555}, John=2231, Inge=1560, Andrii=1))    



#Рекурсія
''' Рекурсивна функція — це функція, що визначається в термінах самої себе і здатна викликати саму себе.
Це означає, що функція викликатиме себе і повторюватиме свою поведінку до тих пір, доки не буде виконана деяка умова для повернення результату.
Найчастіший приклад використання рекурсивних функцій — це обчислення факторіалу. Спершу нагадаємо визначення факторіалу з математики: факторіал натурального числа n визначається як добуток усіх натуральних чисел від 1 до n включно. Наприклад: 5! = 1 · 2 · 3 · 4 · 5 = 120. Це саме визначення можна записати рекурсивно:
    5! = 5 · 4!
    4! = 4 · 3!
    3! = 3 · 2!
    2! = 2 · 1!
    1! = 1
'''
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    

# factorial(5)    # 120

# *********************<<<<<<< Homework 1 >>>>>>>>>>****************

# def greeting():
#     print("Hello world")

# greeting()

# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# def invite_to_event(username):
#     username=f"Dear {username}, we have the honour to invite you to our event"
#     print(username)
#     return username

# invite_to_event("Igor")


# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# base_rate = 40
# price_per_km = 10
# total_trip=0

# def calculate_trip_price(distance_km):
#     total_price=base_rate+price_per_km*distance_km
#     print(total_price)
#     global total_trip
#     total_trip=total_trip+1
#     return total_price

# calculate_trip_price(20)
# calculate_trip_price(4.3)
# print(total_trip)


# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# def func_outer(price,bbb):
#     # x = 5
#     def func_inner():
#         # print("prise test=", price)
#         nonlocal price
#         price = price*bbb
#         print(price)
#     func_inner()
#     return price

# # result = func_outer(10)  # 5
# func_outer(2000, 0.5)


# def discount_price(price, discount):
#     print("Old price - ", price)
#     print("discount -", discount)
#     def apply_discount():
#         nonlocal price
#         price = price*(1-discount)
#         print("price with discount - ", price)
#     apply_discount()
#     return price

# discount_price(100, 0.1)
# discount_price(1000, 0.9) 


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# def get_fullname (first_name,last_name, middle_name=""):
#     if middle_name=="":
#         print(first_name, last_name)
#         return f"{first_name} {last_name}"
#     else:
#         print(first_name, middle_name, last_name)
#         return f"{first_name}  {middle_name} {last_name}"
        
# get_fullname("Andrii", "Petryshyn")
# get_fullname("Igor", "Petryshyn", "Andriyovich")


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# def total(a=6, *pbook, **car):
#     a=1
#     print("a =",a)
#     # прохід по всіх елементах кортежу
#     for sitem in pbook:
#         print('single_item', sitem)

#     #прохід по всіх елементах словника
#     for f_part, s_part in car.items():
#         print(f_part,":",s_part)

# print(total(5, 1, {6}, "a", 5, 2, 3, {"Jack":55555555}, John="2231", Inge=1560, Andrii=1))    



# def first(size, *name):
#     print(size, name)
#     size=size + len(name)
#     print(size)
#     return size

# def second(size, **comments):
#     print(size, comments)
#     size=size + len(comments)
#     print(size)
#     return size

# first(5, "first", "second", "third")
# first(1, "Alex", "Boris")
# second(3, comment_one="first", comment_two="second", comment_third="third")
# second(10, comment_one="Alex", comment_two="Boris")


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# def cost_delivery(quantity, *numbers, discount=0):
#     if discount>0:
#         total_cost=(5+2*(quantity-1))*(1-discount)
#         print(total_cost)
#     elif discount==None:
#         total_cost=(5+2*(quantity-1))
#         print(total_cost)
#     else: total_cost=(5+2*(quantity-1))
#     print(total_cost)
#     return total_cost

# cost_delivery(2, 1, 2, 3)
# cost_delivery(3, 3)
# cost_delivery(1)
# cost_delivery(2, 1, 2, 3, discount=0.5)


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# def fun(a, b=2, c=3):
#     """Знаходить суму трьох параметрів.

#      Перший параметр обов'язковий, два інших за замовчанням дорівнюють 2 і 3"""
#     return a + b * c

# print(fun.__doc__)

# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.
#     Перший параметр &mdash; кількість товарів в замовленні.
#     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result


# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# Обчислюємо факторіал числа n за допомогою рекурсії
# @param n – число, для якого треба розрахувати факторіал
# @return - факторіал числа n
# def factorial(n):
#     fac=0
#     if fac <= 2:
#         return fac  # Базовий випадок
#     else:
#         return n * factorial(n + 1)  # Рекурсивний випадок


# num = int(input("Введіть додатне ціле число: "))
# result = factorial(num)
# print(f"Факторіал числа {num} дорівнює {result}")


# # Мій варіант вичислення факторіалу
# def my_factorial(n):
#     f=1 # тут можна й нуль поставити, на результат не вплине, лише зайвий раз прожене цикл
#     total_fac=1
#     while f<(n):
#         total_fac=total_fac*(f+1)
#         f=f+1
#     print("factorial int n -",total_fac)

# n=int(input("Введіть ціле додатнє число:"))
# result2 = my_factorial(n)
# print(result)

# def factorial(n):
#     f=1 # тут можна й нуль поставити, на результат не вплине, лише зайвий раз прожене цикл
#     total_fac=1
#     while f<(n):
#         total_fac=total_fac*(f+1)
#         f=f+1
#     print("factorial int n -",total_fac)
#     return total_fac

# def number_of_groups(n, k):
#     a=n
#     b=n-k
#     d=k
#     return int(factorial(a)/(factorial(b)*factorial(d)))
#     # print("c=",e)
# print(number_of_groups(50,7))


# Заняття онлайн
# def show_even_square(start,end, step=1):
#     for a in range(start, end+1,step):
#         if a%2==0:
#             print(a," : ", a**2)

# show_even_square(0,20,3)
# show_even_square(1,45,3)
# def add(a,b,*arg):
#     print(arg)
#     print(b)
#     print(a)
#     c=a+b
#     print("c= ",c)
# add(1,3,5,6,7,8,10)




# *********************<<<<<<< Homework 10 >>>>>>>>>>****************
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def fibonachi(n):
#     if n<=1:
#         return 1
#     else:
#         return n





# factorial(5)    # 120
# print(factorial(5))
# n=int(input("Input integer >>>"))
# print(factorial(n))




# def fibonacci(n, memo={}):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n in memo:
#         return memo[n]
#     else:
#         result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#         memo[n] = result
#         return result
#         print(result)

# fibonacci(5)


# def factorial(n):
#     f=1 # тут можна й нуль поставити, на результат не вплине, лише зайвий раз прожене цикл
#     total_fac=1
#     while f<(n):
#         total_fac=total_fac*(f+1)
#         f=f+1
#     print("factorial int n -",total_fac)
#     return total_fac

# def number_of_groups(n, k):
#     a=n
#     b=n-k
#     d=k
#     return int(factorial(a)/(factorial(b)*factorial(d)))
#     # print("c=",e)
# print(number_of_groups(50,7))



# def fibonachi(n)
#     f=0
#     total_fib=0
#     while f<n:
#         f
#         total_fib=total_fib+f


def GetFibonacciList(n, L):
    # Перевірити, чи довжина списку коректна
    count = len(L)
    print("count= ", count)

    # if len(L)<2:
    #     return []

    # Отримати останні числа у списку L
    num1 = L[count-2]
    num2 = L[count-1]
    print(num1)
    print(num2)


    # Формула розрахунку наступного числа
    if (num1+num2) < n:
        L = L + [num1+num2]
        return GetFibonacciList(n, L) # викликати рекурсивно функцію
    else:
        return L # якщо досягнуто кінець, то звичайний вихід

# Викликати функцію GetFibonacciList()
LL = GetFibonacciList(2, [0, 1])
print("LL = ", LL)