# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# import pickle


# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data.bin'

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)


# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)


# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

# -----> Homework

# import pickle


# cont1={
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }
# file1 = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data_hw.bin'

# def write_contacts_to_file(filename, contacts):
#     with open(filename, "wb") as fh:
#         pickle.dump(contacts, fh)
#     return print("Conact added to file data_hw.bin", )

# def read_contacts_from_file(filename):
#     with open(filename, "rb") as fh:
#         unpacked = pickle.load(fh)
#     return unpacked


# a=write_contacts_to_file(file1,cont1)
# print(a)
# print(read_contacts_from_file(file1))



# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# import json

# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
# file_name = 'data.json'

# with open(file_name, "w") as fh:
#     json.dump(some_data, fh)

# with open(file_name, "r") as fh:
#     unpacked = json.load(fh)

# unpacked is some_data  # False
# unpacked == some_data  # False

# unpacked['key'] == some_data['key']  # True
# unpacked['a'] == some_data['a']  # True
# unpacked['2'] == some_data[2]  # True
# unpacked['tuple'] == [5, 6]  # True

# -------> teory 2
# source=[
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# output="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.txt"

# def save_applicant_data(source, output):
#     with open(output, 'w') as f:
#         for student in source:
#             line = f"{student['name']},{student['specialty']},{student['math']},{student['lang']},{student['eng']}\n"
#             f.write(line)

# save_applicant_data(source, output) 

# -----> Homework

# import json

# contacts=[
#     {"name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     },
#     {"name": "Andrii Petryshyn",
#     "email": "andrii@vestibul.co.uk",
#     "phone": "(097) 914-3792",
#     "favorite": True,
#     },
# ]

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data_hw.json'


# def write_contacts_to_file(filename, contacts):
#     with open(filename, "w") as fh:
#         json.dump({"contacts": contacts}, fh)
#     return print("Conact added to file data_hw.json")

# def read_contacts_from_file(filename, key):
#     with open(filename, "r") as fh:
#         unpacked = json.load(fh)
#         if str(key) in unpacked:
#             print(key)
#             return unpacked[str(key)]
#         print(unpacked)


# write_contacts_to_file(file_name,contacts)
# print(read_contacts_from_file(file_name, "contacts"))

# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory

# import csv

# file_name= "c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/expenses.txt"

# with open(file_name, 'w', newline='') as fh:
#     f_n = ['first_name', 'last_name']
#     writer = csv.DictWriter(fh, fieldnames=f_n)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# # Даний код дозволяє зчитати файл навіть якщо не відомі ключі у хедері.
# with open(file_name, newline='') as fh: 
#     line=fh.readline() #читаємо рядок щоб визначити ключі для створення словника k1 v1
#     # for line in read_line:
#     k1, v1 = line.split(",") #розбиваємо рядок на k1 v1
#     # print (k1,v1)
#         # break
#     fh.seek(0) # повертаємось на початок першого рядка
#     reader = csv.DictReader(fh) # починаємо наповнювати словник reader із fh
#     # print (k1,v1)
#     for row_i in reader:
#         print(row_i[str(k1.strip())], row_i[str(v1.strip())]) # підставляємо наші знайдені ключу у першому рядку. 

# -----> Homework

# import csv

# contacts=[
#     {"name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     },
#     {"name": "Andrii Petryshyn",
#     "email": "andrii@vestibul.co.uk",
#     "phone": "(097) 914-3792",
#     "favorite": True,
#     },
#     {"name": "Igor Petryshyn",
#     "email": "igorp@vestibul.co.uk",
#     "phone": "(073) 914-3792",
#     "favorite": False,
#     },
# ]

# file_name= "c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/names_hw.csv"


# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w', newline='') as fh:
#         f_n = ["name", "email","phone","favorite"]
#         writer = csv.DictWriter(fh, fieldnames=f_n)
#         writer.writeheader()
#         for cont in contacts:
#             writer.writerow({'name': cont["name"], "email": cont["email"], "phone":cont["phone"], "favorite":cont["favorite"] })
#     return print("All contacts added to file")

# def read_contacts_from_file(filename):
#     list_contacts=[]
#     with open(filename,"r", newline='') as fh: 
#         reader = csv.DictReader(fh) 
#         for row_i in reader:
#             row_i["favorite"]=row_i["favorite"] =="True"
#             list_contacts.append(row_i)
#         return list_contacts


# write_contacts_to_file(file_name,contacts)
# print(read_contacts_from_file(file_name))

# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# import pickle


# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data.bin'

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)


# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)


# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

# -----> Homework

# import pickle

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data_hw.bin'

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name=name
#         self.email=email
#         self.phone=phone
#         self.favorite=favorite
      

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename=filename
#         self.contacts=contacts
#         if contacts is None:
#             contacts = []
   
#     def save_to_file(self):
#         with open(self.filename, "wb") as fh:
#             # pickle.dump(self.contacts,  fh) # такий код передає лише contacts
#             pickle.dump(self,  fh) # такий варіант коду передає (зберігає) екземпляр класу Contacts 
#             print ("contscts added to binary file")

#     def read_from_file(self):
#         with open(self.filename, "r") as fh:
#             unpacked=pickle.load(fh)
#             print(unpacked)
#         return unpacked


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory

# -----> Homework

# import pickle

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data_hw.bin'

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.count_save=0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content
    
#     def __getstate__(self):
#         atributes=self.__dict__.copy()
#         atributes["count_save"]+=1
#         return atributes

# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory

# -----> Homework

# import pickle

# file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data_hw.bin'

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.count_save=0
#         self.is_unpacking=False

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content
    
#     def __getstate__(self):
#         atributes=self.__dict__.copy()
#         atributes["count_save"]+=1
#         return atributes
    
#     def __setstate__(self, value):
#         self.__dict__.update(value)
#         self.is_unpacking=True


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# import copy

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def copy_class_person(person):
#     copy_class=copy.copy(person)
#     return copy_class


# person = Person(
#     "Allen Raymond",
#     "nulla.ante@vestibul.co.uk",
#     "(992) 914-3792",
#     False,
# )

# copy_person = copy_class_person(person)

# print(copy_person == person)  # False
# print(copy_person.name == person.name)  # True

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# import copy
# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def copy_class_person(person):
#     return copy.copy(person)


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] = attributes["count_save"] + 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True


# def copy_class_contacts(contacts):
#     class_deepcopy=copy.deepcopy(contacts)
#     return class_deepcopy



# contacts2 = [
#     Person(
#         name="Allen Raymond",
#         email="nulla.ante@vestibul.co.uk",
#         phone="(992) 914-3792",
#         favorite=False,
#     ),
#     Person(
#         name="Andrii Petryshyn",
#         email="andrii@vestibul.co.uk",
#         phone="(097) 914-3792",
#         favorite=True,
#     ),
#     Person(
#         name="Igor Petryshyn",
#         email="igorp@vestibul.co.uk",
#         phone="(073) 914-3792",
#         favorite=False,
#     ),
# ]


# persons = Contacts("user_class.dat", contacts2)
# print(persons.contacts[0].name)
# new_persons = copy_class_contacts(persons)

# new_persons.contacts[0].name = "Another name"

# print(persons.contacts[0].name)  
# print(new_persons.contacts[0].name)  # Another name

# print("")
# print("class persons", persons)
# print("")

# print("class new_perssns", new_persons)


# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# from copy import deepcopy, copy


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

#     def __copy__(self):
#         copy_class_p=Person(self.name, self.email, self.phone, self.favorite)
#         return copy_class_p


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] = attributes["count_save"] + 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True

#     def __copy__(self):
#         copy_class_c=Contacts(self.filename,self.contacts)
#         return copy_class_c

#     def __deepcopy__(self, memo):
#         dcopy = Contacts(self.filename, copy.deepcopy(self.contacts, memo))
#         memo[id(self)] = dcopy
#         return dcopy


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
