# from collections import UserDict

# class Field: 
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     pass

# class Phone(Field):
#     def __init__(self, phone):
#         if len(phone) >= 10 :
#             super().__init__(phone)
#         else:
#             raise ValueError

# class Record:
#     def __init__(self, name_r):
#         self.name = Name(name_r)
#         self.phones = [] # [Phone('1234222')]

#     # реалізація класу
#     def find_phone(self, phone):
#         for user_phone in self.phones:
#             if user_phone.value == phone:
#                 print("find user_phone is", user_phone)
#                 return user_phone

#     def add_phone(self, phone_r):

    
    
#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     def __int__(self):
#         self.data = []
#     # def add_record(self, name, phone)
#     def add_record(self, record):
#         # name = record.name.value
#         self.data = record
    
#     def all_book(self):
#         return str(self.data)

    
# record = Record('Oleg')
# record.phones.append(Phone('1234453568'))
# print(record)

# phone_find = record.find_phone('1234453568')
# print(phone_find)
# phone_find.value = '0987654335'
# print(record)

# addressBook = AddressBook()
# addressBook.add_record(record)
# print(addressBook.all_book())

# record2=Record("Andrii")
# addressBook.add_record(record2)
# print(addressBook.all_book())



