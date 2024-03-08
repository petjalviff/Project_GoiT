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



class Person:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34, 1231232312, "boris@com.ua")
print(p.name)  # Boris
print(p.age)  # 34
print(p.greeting())  # Hi Boris
print(p.email)
print(p.phone)
p.name="Andrii"
print(p.name)
