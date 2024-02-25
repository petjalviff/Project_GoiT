# import shutil

# for a, b, in shutil.get_archive_formats():
#     print("_"*40)
#     print("{:^
#           10} | {:^25} |".format(a,b))


# f=open("e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt", mode="x+")

# f.write("\nMy first create file 2")
# f.seek(0)
# print(f.readlines())


# f.close() 

# with open("e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt", mode="w+") as f:
#     text=f.read()
#     # print(f.read())
#     print(text)
#     f.write("My first create file 2 from with")
#     f.seek(0)
#     text=f.read()
#     print(text)


# from faker import Faker


# fake=Faker()


# def get_mocked_user():
#     return{
#         "name":fake.name(),
#         "last_name": fake.last_name(),
#         "email": fake.email(),
#     }


# if __name__ == "__main__":
#     user=get_mocked_user()



# *********************<<<<<<< Homework1 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# employee_list=[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt"

# def write_employees_to_file(employee_list, path):
#     f=open(path, mode="w")
#     for i in employee_list:
#         for a in i:
#             print(a)
#             f.writelines(a+"\n")
#     f.close() 

# write_employees_to_file(employee_list,path)



# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt"

# def read_employees_from_file(path):
#     employee_list=[]

#     f=open(path, mode="r")
#     for line in f:
#         employee = line.strip()
#         employee_list.append(employee) 
        
#     f.close()
#     return employee_list 

# print(read_employees_from_file(path))


# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# record="Drake Mikelsson,19"
# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt"

# def add_employee_to_file(record, path):
#     f=open(path, mode="a")
#     f.write(record+"\n")
#     f.close() 

# add_employee_to_file(record, path)


# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.txt"

def get_cats_info(path):
    cats_dict=[]

    with open(path, mode="r") as f:
        for line in f:
            employee = line.strip()
            # print(employee)
            line_split=employee.split(",")
            # print(line_split)
            # print(line_split[0])
            # print(line_split[1])
            # print(line_split[2])
            cats_dict.append({
                "id":line_split[0],
                "name":line_split[1],
                "age":line_split[2],
            })
        
    
    return cats_dict 

print(get_cats_info(path))


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework



# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
