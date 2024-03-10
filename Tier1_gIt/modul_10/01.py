# class User:
#     name = 'UserName'
#     age = 15

#     def say_name(self):
#         print(f'Hi! I am {self.name} and I am {self.age} years old.')

#     def set_age(self, age_new):
#         self.age = age_new
#         print(f'Now I have {self.age} years old.')


# bob = User()
# bob.name = 'Andrii'
# bob.age = 35

# bob.say_name()  # Hi! I am Bob and I am 15 years old.

# bob.set_age(25)
# bob.say_name()  # Hi! I am Bob and I am 25 years old.



# class Person:
#     def __init__(self, name, age, phone, email):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.email = email

#     def greeting(self):
#         return f"Hi {self.name}"


# p = Person("Boris", 34, 1231232312, "boris@com.ua")
# print(p.name)  # Boris
# print(p.age)  # 34
# print(p.greeting())  # Hi Boris
# print(p.email)
# print(p.phone)
# p.name="Andrii"
# print(p.name)



# class Human:
#     name = ''
#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""
#     def make_some_code(self):
#         return f"{self.field_description} is {self.hhhh}"


# class PythonDeveloper(Developer):
#     hhhh = "Python"


# class JSDeveloper(Developer):
#     hhhh = "JavaScript"


# p_dev = PythonDeveloper()
# # p_dev.name = 'Bob'
# print(p_dev.voice())   # Hello! My name is Bob
# print(p_dev.make_some_code())  # My Programming language is Python


# js_dev = JSDeveloper()
# js_dev.make_some_code()  # My Programming language is JavaScript

# countable = [1, '2', 3, '4']

# d_sum = sum(map(lambda x: int(x), countable))

# countable.append('5')


# print(d_sum)

# from collections import UserString

# class TruncatedString(UserString):
#     MAX_LEN = 7
#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]

# ts = TruncatedString('abcdefghjklmnop')
# ts.truncate()
# print(ts)   # вивід abcdefg
# ts.MAX_LEN=10
# ts.truncate()
# print(ts)  # abcdefg



# import string


# class NameTooShortError(Exception):
#     pass

# class NameStartsFromLowError(Exception):
#     pass

# class NameOnlyLeters(Exception):
#     pass

# def enter_name():
#     name = input("Enter name: ")
#     def is_ascii_letters_only(name):
#         return all(char in string.ascii_letters for char in name)
#     if len(name) < 3:
#         raise NameTooShortError
#     if name[0] not in string.ascii_uppercase:
#         raise NameStartsFromLowError
#     if is_ascii_letters_only:
#         raise NameOnlyLeters

# while True:
#     try:
#         name = enter_name()
#         break
#     except NameTooShortError:
#         print('Name is too short, need more than 3 symbols. Try again.')
#     except NameStartsFromLowError:
#         print('Name should start from capital letter. Try again.')
#     except NameOnlyLeters:
#         print ("Name must have only leters")

# class Mammal:
#     phrase = '1'
#     def voice(self):
#         return self.phrase


# class Dog(Mammal):
#     phrase = 'Bark!'



# class Cat(Mammal):
#     phrase = 'Meow!'


# class Chupakabra:
#     hghghgh="1111112"
#     def voice(self):
#         # return 'Whooooo!!!'
#         return self.hghghgh


# class Recorder:
#     def record_animal(self, animal):
#         voice2 = animal.voice()
#         print(f'Recorded "{voice2}"')


# r = Recorder()
# cat = Cat()
# dog = Dog()
# strange_animal = Chupakabra()

# r.record_animal(cat)            # Recorded "Meow!"
# r.record_animal(dog)            # Recorded "Bark!"
# r.record_animal(strange_animal) # Recorded "Whooooo!!!"


