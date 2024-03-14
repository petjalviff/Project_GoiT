# # # *********************<<<<<<< 1. Серіалізація об'єктів Python >>>>>>>>>>****************

# # expenses = {
# #     "hotel": 150,
# #     "breakfast": 30,
# #     "taxi": 15,
# #     "lunch": 20
# # }


# # file_name = "c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/expenses.txt"
# # # with open(file_name, "w") as fh:
# # #     for key, value in expenses.items():
# # #         fh.write(f"{key}|{value}\n")


# # file_name = "c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/expenses.txt" #['hotel|150\n', 'breakfast|30\n', 'taxi|15\n', 'lunch|20\n']
# # expenses2 = {}
# # with open(file_name, "r") as fh:
# #     raw_expenses = fh.readlines() 
# #     print(raw_expenses) #['hotel|150\n', 'breakfast|30\n', 'taxi|15\n', 'lunch|20\n']
# #     for line in raw_expenses:
# #         k1, v1 = line.split(",")
# #         print (k1, v1)
# #         expenses2[k1] = int(v1)

# # print(expenses2) # {'hotel': 150, 'breakfast': 30, 'taxi': 15, 'lunch': 20}

# # *********************<<<<<<< 2. ССеріалізація об'єктів Python за допомогою pickle >>>>>>>>>>****************

# # import pickle


# # some_data = {
# #     (1, 3.5): 'tuple',
# #     2: [1, 2, 3],
# #     'a': {'key': 'value'}
# # }

# # byte_string = pickle.dumps(some_data)
# # unpacked = pickle.loads(byte_string)

# # print(unpacked == some_data)    # True
# # print(unpacked is some_data)    # False


import pickle


some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)


with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)


print(unpacked == some_data)    # True
print(unpacked is some_data)    # False


# # *********************<<<<<<< 3. Серіалізація об'єктів Python за допомогою json >>>>>>>>>>****************

# # import json


# # some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

# # byte_string = json.dumps(some_data)
# # unpacked = json.loads(byte_string)

# # unpacked is some_data    # False
# # unpacked == some_data    # False

# # print(unpacked['key'] == some_data['key'])     # True
# # print(unpacked['a'] == some_data['a'])         # True
# # print(unpacked['2'] == some_data[2])           # True
# # print(unpacked['tuple'] == [5, 6])             # True



# # import json


# # some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
# # file_name = 'c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/data.json'

# # with open(file_name, "w") as fh:
# #     json.dump(some_data, fh)


# # with open(file_name, "r") as fh:
# #     unpacked = json.load(fh)
    

# # print(unpacked)

# # unpacked is some_data    # False
# # unpacked == some_data    # False

# # unpacked['key'] == some_data['key']     # True
# # unpacked['a'] == some_data['a']         # True
# # unpacked['2'] == some_data[2]           # True
# # unpacked['tuple'] == [5, 6]             # True


# # *********************<<<<<<< 4. Робота з таблицями CSV у Python >>>>>>>>>>****************

# # import csv


# # with open('c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/eggs.csv', 'w', newline='') as fh:
# #     spam_writer = csv.writer(fh)
# #     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
# #     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# # with open('c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/eggs.csv', newline='') as fh:
# #     spam_reader = csv.reader(fh)
# #     for row in spam_reader:
# #         print(', '.join(row))


# import csv

# file_name= "c:/Project_GoiT/Project_GoiT/Tier1_gIt/modul_12/expenses.txt"

# # with open(file_name, 'w', newline='') as fh:
# #     f_n = ['first_name', 'last_name']
# #     writer = csv.DictWriter(fh, fieldnames=f_n)
# #     writer.writeheader()
# #     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# #     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
# #     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

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

# # print (reader)

# #*********************<<<<<<< 5. Управління порядком серіалізації >>>>>>>>>>****************


# #*********************<<<<<<< 6. Створення копій об'єктів Python >>>>>>>>>>****************

# import copy


# my_list = [1, 2, {1: 'a'}]
# copy_list = copy.deepcopy(my_list)
# copy_list.append(4)
# print(my_list)      # [1, 2, {1: 'a'}]
# print(copy_list)    # [1, 2, {1: 'a'}, 4]

# copy_list[2][2] = 'b'
# print(my_list)    # [1, 2, {1: 'a', 2: 'b'}]
# print(copy_list)


# # *********************<<<<<<< 2. ССеріалізація об'єктів Python за допомогою pickle >>>>>>>>>>****************


import pickle

import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, count_save: int = 0, is_unpacking: bool = False):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save
        self.is_unpacking = is_unpacking

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    
    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        state = self.__dict__.copy()
        state['count_save'] += 1
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_unpacking = True