# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")
# a=bool(is_active)
# b=bool(is_admin)
# c=bool(is_permission)
# access = b or (a and c)
# is_active = bool(input("Is the user active? "))
# is_admin = bool(input("Is the user administrator? "))
# is_permission = bool(input("Does the user have access? "))

# access=is_admin or (is_active and is_permission)
# print (access)


# # Завдання 3
# work_experience = int(input("Enter your full work experience in years: "))
# a=work_experience
# if a>1 and a<=5:
#     developer_type = "Middle"
# elif a<=1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)
# print("Далі буде тест")

# # Test Homework 3
# a=0
# while a<=8:
#     if a>1 and a<=5:
#         developer_type = "Middle"
#     elif a<=1:
#         developer_type = "Junior"
#     else:
#         developer_type = "Senior"
#     print(a)
#     print(developer_type)
#     a=a+1



# Homework 4

# num = int(input("Enter a number: "))

# if num>0:
#     if num>0 and num%2:
#         result = "Positive odd number"

#     else:
#         result = "Positive even number"
# elif num<0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)




# Homework 5

# import math

# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c
# print(f"D={D}")
# if D>0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     print(f"x1={x1}")
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(f"x2={x2}")
# else: print("equation do not have real roots")



#Homework 6

# num = int(input("Enter an integer number: "))
# if num%2:
#     is_even=False
# else: is_even=True
# print(is_even)


# Homwork 7

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# a=1
# while a<=num:
#     sum=sum+a
#     print(f"ітерація {a} : {sum}")
#     a=a+1
# else:print(f"сума всіх чисел від 0 до {num} становить {sum}")


#Homework 8

# fruit = 'apple'
# a=0
# for char in fruit:
#     if char=="p":
#         print(char)
#         a=a+1
#     else: print("not p")
# print(a)
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = input("Input search char: ")
# result = 0
# for char in message:
#     if char==search:
#         result=result+1
#         print(result)
#         print(char)
# text= f"В даному виразі є {result}  літер {search}"
# print(text)

# Homework 9
# while True:
#     num = int(input("Введіть число (0 для виходу) або більше щоб продовжити: "))
#     if num == 0:
#         break
#     repeat = int(input("Скільки разів помножити число на 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num==0:
#         break
#     sum=0
#     for i in range(num + 1):
#         sum = sum + i
#     print(sum)


# Homework 10
# a=int(input("Enter Integer from 0 to 100: "))
# print (a)
# # b=a%2
# # print(b)
# sum=0
# for c in range(a+1):
#     if c%2==0:
#         sum=sum+c
#         # print(c)
#         continue
#     # print(c)
#     # sum=sum+c
# print(sum)

# num = int(input("Enter Integer: "))
# for variable in range(num):
#     if variable % 2 == 1:
#         continue
#     print(variable)

# while True:
#     num = int(input("Enter integer (0 for output): "))
#     sum = 0
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i%2==1:
#             continue

#         sum = sum + i
#     print(sum)


# Homework 11
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""

# for ch in message:
#     if 'a' <= ch <= 'z':
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord('a'))
#         encoded_message += new_char
#         # print(encoded_message)
#     elif 'A' <= ch <= 'Z':
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord('A'))
#         encoded_message += new_char
#         # print(encoded_message)
#     else:
#         encoded_message += ch
#     print(encoded_message)


# ch=input("Enter character: ")
# position=ord(ch)
# print(position)
# # # while ch<"z":
# # print(position)

# # ch=chr(position+1)
# print(ch)
# a=ord(ch)
# sms=ch
# encode_sms=(chr(a)+1)
# while ch <"z":
    
#     a=a+1
#     print(a)
#     ch=chr(a)
#     print(ch)
#     sms=sms+ch
#     # print(sms)
#     # if a>ord("z"):
#     #     break
# print("Hello")
# print(sms)


#Homework 12
# try:
#     num = int(input("Введіть розмір команди: "))
#     award = 10000
#     bonus_for_person = award / num
# except ValueError:
#     print("Ви ввели не число!")
# except ZeroDivisionError:
#     print("Ви ввели нуль учасників!")
# else:
#     print(f"Нагорода кожному учаснику {bonus_for_person} золота!")
# finally:
#     print("До побачення!")

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool//quantity
# except ValueError:
#     print("You enterned not Integer!")
# except ZeroDivisionError:
#     print("You enterned zero!")
# else: print(f"You send {chunk} SMS")
# finally:
#     print('Divide by zero completed!')
