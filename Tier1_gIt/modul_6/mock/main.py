from mock import get_mocked_user

from pprint import pprint
import json
amount=int(input("How many users you need >>>"))

users = list()
for _ in range(amount):
    users.append(get_mocked_user())

# pprint(users) 
with open("e:/Projects/Project_GoiT/Tier1_gIt/modul_6/mock/user.json", mode="w") as f:
    text =json.dumps(users)
    f.writelines(text)