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

# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.txt"

# def get_cats_info(path):
#     cats_dict=[]

#     with open(path, mode="r") as f:
#         for line in f:
#             employee = line.strip()
#             # print(employee)
#             line_split=employee.split(",")
#             # print(line_split)
#             # print(line_split[0])
#             # print(line_split[1])
#             # print(line_split[2])
#             cats_dict.append({
#                 "id":line_split[0],
#                 "name":line_split[1],
#                 "age":line_split[2],
#             })
        
    
#     return cats_dict 

# print(get_cats_info(path))


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# source="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data2.txt"
# output="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.txt"

# def sanitize_file(source, output):
   
#     with open(source, 'r') as source_file:  
#         text = source_file.read()
    
#     clear_text = ''.join(char for char in text if not char.isdigit())
#     # clear_text=()
#     # for char in text:
#     #      if not char.isdigit:
#     #         clear_text="".join(char)
#     # print(clear_text)
#     with open(output, 'w') as output_file:
#             output_file.write(clear_text)

# sanitize_file(source, output)


# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework
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
    


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# utf8_string = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82'
# utf16_string = b'\xff\xfe\xd0\x9f\x00\r\x00\x96\x00\x98\x00\x82\x00'

# def is_equal_string(utf8_string, utf16_string):
#     try:
       
#         utf8_decoded = utf8_string.decode('utf-8')
#         utf16_decoded = utf16_string.decode('utf-16')  # 
#         return utf8_decoded == utf16_decoded
#     except UnicodeDecodeError:
        
#         return False


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.bin"
# users_info={'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

# def save_credentials_users(path, users_info):
#     with open(path,'wb') as f:
#         for username,password in users_info.items():
#             text_info = f"{username}:{password}\n"
#             print(text_info)
#             text_bin=text_info.encode()
#             f.write(text_bin)

# save_credentials_users(path, users_info)



# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# -----> Homework
     
# path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6/data.bin"

# def get_credentials_users(path):
#     with open(path,"rb") as file:
#         list=[]
#         for line in file:
#             text=line.decode()
#             text=text.strip()
#             print(text)
#             list.append(text)
#     print(list)
#     return list

# get_credentials_users(path)



# *********************<<<<<<< Homework 10 >>>>>>>>>>****************
# -------> theory
# -----> Homework
import shutil

employee_residence={'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
path="e:/Projects/Project_GoiT/Tier1_gIt/modul_6"
file_name="data2.bin"

def create_backup(path, file_name, employee_residence):
    path2=path+"/"+file_name

    with open(path2,'wb') as f:
        for username,password in employee_residence.items():
            text_info = f"{username} {password}\n"
            print(text_info)
            text_bin=text_info.encode()
            f.write(text_bin)
    backup_folder="backup_folder"
    backup_path=path+"/"+backup_folder+".zip"
    
    # backup_path_f=backup_path+".zip"
    return shutil.make_archive(backup_path, "zip", path )

print(create_backup(path, file_name, employee_residence))

# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
