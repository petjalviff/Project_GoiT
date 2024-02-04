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
