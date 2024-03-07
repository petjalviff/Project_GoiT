# numbers1 = ([1], [2], [3])
# numbers2 = (1, 2, 3, 4, 5)
# numbers3 = [(1), (2), (3), (4), (5)]


# # for i in map(lambda x: x+5, numbers1):
# #     print(i)

# for i in map(lambda x: x+5, numbers2):
#     print(i)

# for i in map(lambda x: x+5, numbers3):
#     print(i)


# for i in filter(lambda x: x % 2, range(1, 10+1)):
#     print(i)

some_str = 'aaAbbB C F DDd EEe'
a=[]
for i in filter(lambda x: x.islower(), some_str):
    a.append(i*2+".")
    a.reverse()
    print(i)
    print(a)


