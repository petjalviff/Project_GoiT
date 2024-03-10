# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)


# def get_student_grade(option):
#     if option =="grade":
#         return get_grade
#     elif option == "description":
#         return get_description
    
# student_grade=get_student_grade("description")
# print(student_grade("E"))

# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# DEFAULT_DISCOUNT=0.05
# price=100
# customer1={"name": "Boris", "discount": 0.15}
# customer2={"name": "Dima"}

# customer = customer1

# def get_discount_price_customer(price, customer):
#     len_cust=len(customer)
#     # print(len_cust)
#     if len_cust ==2:
#         discount=customer["discount"]
#         price = price * (1 - discount)
#         # print(price)
#     else :
#         discount=DEFAULT_DISCOUNT
#         price = price * (1 - discount)
#         # print(price)
#     return price

# print(get_discount_price_customer(price,customer))


# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# def caching_fibonacci():
#     cache = {}

#     def fibonacci(n):
#         if n in cache:
#             return cache[n]
#         if n <= 1:
#             return n
#         else:
#             result = fibonacci(n - 1) + fibonacci(n - 2)
#             cache[n] = result
#             print(result)
#             return result
#     print(cache)        
#     return fibonacci

# fib=caching_fibonacci()

# print(fib(15))


# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework



# def discount_price(discount):
#     def calculate_price(price):
#         return price * (1 - discount)

#     return calculate_price

# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory

# def logged_func(func):
#     def inner(a, b):
#         print(f'called with {a}, {b}')
#         result = func(a, b)
#         print(f'result: {result}')
#         return result
#     return inner


# @logged_func
# def complicated(x, y):
#     i=x*y
#     return i

# print(complicated(10,2))


# -----> Homework
# phone="    +38060)123-32-34"

# def format_phone_number(func1):
#     def format_number(phone_numb):
#         res= func1(phone_numb)
#         print(res)
#         if len(res) == 10:
#             res="+38"+res
            
#         elif len(res)==12:
#             res="+"+res
            
#         else:
#             print(res, "is ucnown number")
#         return res
#     return format_number


# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone
# print(sanitize_phone_number(phone))


# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# def normal_name(names):
#     return list(map(lambda x: x.capitalize(), names))

# name = ["dan", "jane", "steve", "mike"]
# name_norm = normal_name(name)
# print(name_norm)


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework


# def get_emails(list_contacts):
#     #функція для витягування email зі словника контакту
#     def email_ext(email):
#         return email['email']

#     emails_all = list(map(email_ext, list_contacts))
#     return emails_all

# # Приклад використання
# contacts = [
#     {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
#     {"name": "John Doe", "email": "john.doe@example.com", "phone": "(123) 456-7890", "favorite": True},
#     {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "(987) 654-3210", "favorite": False}
# ]

# emails_list = get_emails(contacts)
# print(emails_list)

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework


payment = [100, -3, 400, 35, -100]

def positive_values(list_payment):
    list_value=[]
    for a in filter(lambda y:y>=0,list_payment):
        list_value.append(a)
    return list_value


print(positive_values(payment))

# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# contacts = [
#     {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
#     {"name": "John Doe", "email": "john.doe@example.com", "phone": "(123) 456-7890", "favorite": True},
#     {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "(987) 654-3210", "favorite": False}
# ]

# def get_favorites(contacts):
#     #функція для витягування favorite зі словника контакту
#     def favorite_ext(favorite):
#         print(favorite['favorite'])
#         return favorite['favorite']
#         # return True
    

#     favorite_all = list(filter(favorite_ext, contacts))
#     return favorite_all



# favorite_list = get_favorites(contacts)
# print(favorite_list)



# *********************<<<<<<< Homework 10 >>>>>>>>>>****************
# -------> theory
# numbers = [3, 4, 6, 9, 34, 12]
# sum=0
# for a in numbers:
#     sum=sum+a

# print(sum)
# -----> Homework

# from functools import reduce

# numbers = [3, 4, 6, 9, 34, 12]

# def sum_numbers(numbers):
#     sum=reduce((lambda x, y: x+y), numbers)
#     return sum
# print (sum_numbers(numbers))

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
