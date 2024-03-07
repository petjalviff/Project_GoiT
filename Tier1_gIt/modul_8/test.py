from collections import namedtuple

# Оголошуємо іменований кортеж
Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

cats1=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats2=[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


# Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

for i in cats1:
    print(i)

# cat_list=Cat("Mick", 5, "Sara")

# print(cat_list)