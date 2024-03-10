# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     animal_name=""
# animal=Animal()

# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname=nickname
#         self.weight=weight
    
#     def say(self):
#         pass



# animal=Animal("Boris",10)

# print(animal.nickname)
# print(animal.weight)

# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname=nickname
#         self.weight=weight
    
#     def say(self):
#         pass
    
#     def change_weight(self, weight_new):
#         self.weight=weight_new


# animal=Animal("Simon",10)

# print(animal.nickname)
# print(animal.weight)
# animal.change_weight(12)
# print(animal.weight)

# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
    
#     def change_color(self, color_new):
#         self.color=color_new


# first_animal=Animal("Simon",10)
# second_animal=Animal("Vaska",9)


# first_animal.change_color("red")
# print(first_animal.color)
# print(second_animal.color)

# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"
    

# cat=Cat("Simon", 10)

# print(cat.say())


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name=name
#         self.age=age
#         self.address=address
    
#     def info(self):
#         info_dict={
#             "name":self.name,
#             "age":self.age,
#             "address":self.address
#         }
#         return info_dict
    

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         super().__init__(nickname, weight) 
#         self.breed=breed
#         self.owner=owner

#     def say(self):
#         return "Woof"
    
#     def who_is_owner(self):
#         return owner.info()
    

# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Barbos", 23, "labrador", owner)


# print(owner.info())
# print(dog.who_is_owner())

# print(dog.nickname)
# print(dog.weight)
# print(dog.breed)
# print(dog.say())

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# from collections import UserList


# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         sum = 0
#         for i in self.data:
#             if i > 0:
#                 sum = sum + i
#         return sum

# payment = AmountPaymentList([1, -3, 4])
# print(payment.amount_payment())

# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# from collections import UserList

# class NumberString1(UserList):
#     def number_count(self):
#         count=0
#         for i in self.data:
#             print(i)
#             count=count+1
#         return count


# count1 = NumberString1([1, '2', 3, '4'])
# count1.append('5')
# print(count1.number_count())     # 15



# -----> Homework

# from collections import UserString


# class NumberString(UserString):
#     def number_count(self):
#         count=0
#         for i in self.data:
#             if i.isdigit():
#                 print(i)
#                 count=count+1
#         return count


# count = NumberString([1, '2', 3, '4'])
# print(count.number_count())

# *********************<<<<<<< Homework 10 >>>>>>>>>>****************
# -------> theory
# -----> Homework


# class IDException(Exception):
#     pass

# def add_id(id_list, employee_id):
#     if employee_id.startswith("01"):
#         id_list.append(employee_id)
#     else: 
#         raise IDException("Employee ID must start with '01'")
#     return id_list

# new_employee_id="01hd"
# new_id_list=['0101', '0123']

# print(add_id(new_id_list,new_employee_id))


# *********************<<<<<<< Homework 11 >>>>>>>>>>****************
# -------> theory

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.cat=Cat(nickname, weight)

    def say(self):
        return self.cat.say()
    
    def change_weight(self, weight):
        self.weight = weight
    
cat_dog=CatDog("Kitty", 5)
print(cat_dog.say())


cat=Cat("Simon",5)
print(cat.nickname)
cat.weight=45
print(cat.weight)


# -----> Homework


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#         self.cat=Cat(nickname, weight)

#     def say(self):
#         return self.cat.say()
    
#     def change_weight(self, weight):
#         self.weight = weight
    
# cat_dog=CatDog("Kitty", 5)
# print(cat_dog.say())

# *********************<<<<<<< Homework 12 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite=False):
#         contact={
#                         "id": Contacts.current_id,
#                         "name": name,
#                         "phone": phone,
#                         "email": email,
#                         "favorite": favorite
#                     }
#         self.contacts.append(contact)
#         Contacts.current_id =Contacts.current_id+1

# contact1=Contacts()
# contact1.add_contacts("Andrii Petryshyn", "123456789", "andrii@com.net", True)
# print(contact1.list_contacts())
# contact1.add_contacts("Igor Petryshyn", "987654321", "igor@com.net", True)
# print(contact1.list_contacts())


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework