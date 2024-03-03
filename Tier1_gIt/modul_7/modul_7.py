
# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# -----> Homework


# from setuptools import setup

# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }


# def do_setup(args_dict):
#     setup(**args_dict)


# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# from setuptools import setup


# def do_setup(args_dict, requires):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,)


# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# def data_preparation(data):
#     merged_list = []
#     for sublist in data:
#         if len(sublist) > 2:
#             sublist.remove(max(sublist))
#             sublist.remove(min(sublist))
#         merged_list.extend(sublist)
#     return sorted(merged_list, reverse=True)

# Приклад використання:
# list_data = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
# def data_preparation(list_data):
#     list_all=[]
#     for list in list_data:
#         if len(list)>2:
#             list.remove(max(list))
#             list.remove(min(list))

#         list_all.extend(list)

#     list_all.sort()
#     list_all.reverse()
#     # print(list_all)
#     print(list_all)
#     return list_all
# print(data_preparation(list_data))


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# def all_sub_lists(lst):
#     n=len(lst)+1
#     sub_lists = [[]]
#     k=1
#     while k<n+1:
#         for j in range(len(lst)):
#             i=j+k
#             if i<n:
#                 sub_lists.append(lst[j:i])
#         k=k+1
#     return sub_lists

# my_list = [4, 6, 1, 3, 8, 9, 12]
# result = all_sub_lists(my_list)
# print(result)


# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# list_1=("Afdsgh", "Bsdfh", "Chfdgh", "Dasdfas", "Ehdfsf", "FXhdshd")
# list_2=("Afdsgh", "Bsdfh", "Chfdgh", "Dasdfas", "Ehdfsf", "FXhdshd", "Fasf")

# def make_request(keys, values):
#     list1=keys
#     list2=values
#     dict_request={}
#     n=len(list1)
#     if len(list1)==len(list2):
#         for i in range(n):
#             l1=list1[i]
#             l2=list2[i]
#             dict_request[f"{l1}"]=f"{l2}"
#             i=i+1
#     print(dict_request)
#     return dict_request

# make_request(list_1,list_2)

# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# path="C:\Project_GoiT\Project_GoiT\Tier1_gIt\modul_7\data23.txt"
# additional_info="\nHello Igor, what are you do?"
# start_pos=5
# count_chars=15

# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path,"a") as file:
#         file.write(additional_info)
#     with open(path,"r") as file:
#         file.seek(start_pos)
#         text=file.read(count_chars)
#         print(text)

# file_operations(path, additional_info, start_pos, count_chars)

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# path="C:\Project_GoiT\Project_GoiT\Tier1_gIt\modul_7\data23.txt"
# profession=("courier" )

# def get_employees_by_profession(path, profession):
#     with open(path,"r") as file:
#         lines=file.readlines()
#         # print(lines)
#         text=[]
#         for line in lines:
#             line.find(profession)
#             # print(line)
#             if line.find(profession) !=-1:
#                 line=line.replace(profession,"")
#                 line=line.strip()

#                 text.append(line)
#         print(text)
#         # clean_text=text.str
#         res_text=" ".join(text)
#         print(res_text)
#         # res_text=res_text.replace(profession, "")
#     print (res_text)
#     return res_text



# get_employees_by_profession(path, profession)


# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# source_file="C:\Project_GoiT\Project_GoiT\Tier1_gIt\modul_7\data23.txt"
# output_file="C:\Project_GoiT\Project_GoiT\Tier1_gIt\modul_7\data24.txt"

# def to_indexed(source_file, output_file):
#     with open(source_file,"r") as file:
#         lines=file.readlines()
#     text=[]
#     i=0
#     for line in lines:
#         text.append(f"{i}: {line}")
#         i=i+1
#     print(text)
#     with open(output_file, "w") as file:
#         for a in text:
#             file.write(a)
#     return text

# to_indexed(source_file, output_file)


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
