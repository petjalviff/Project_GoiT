phone=[]
new_phone="1234567892"
phone.append(new_phone)
print(phone)
new_phone="1232123123"
phone.append(new_phone)
print(phone)
# phone.clear()
# phone_remove="1232123123"
# phone.remove(phone_remove)
print(phone)
name="Andrii"

contact={
    "name":name,
    "phone":phone
}

print(contact)
adress_book=[]
adress_book.append(contact)
print(adress_book)

contact2={
    "name":"Igor",
    "phone":["111111111111","2222222222"]
}

print(contact2.get("phone"))

adress_book.append(contact2)
print(adress_book)
print("*"*30)

name_find1="Andrii"

def find_phone(phone_find, contact_finded):
    for i in contact_finded["phone"]:
        if i == phone_find:
            print(i)
            print(contact_finded["name"])
    return contact_finded


def find_name(name_find, adr_book):
    for i in adr_book:
        if name_find == i.get("name"):
            print(i)
            print(i.get("name"))
        return i

contact_find=find_name(name_find1,adress_book)


print(contact_find)
contact_find["phone"].append("555555555555")
print(contact_find)
# adress_book.remove(name_find1)
print(adress_book)
# adress_book.append(contact_find)
# print(adress_book)

phone_find1=find_phone("555555555555", contact_find)
# contact_find["phone"]. # поки не ясно як видалити конкретний телефон
print(phone_find1)