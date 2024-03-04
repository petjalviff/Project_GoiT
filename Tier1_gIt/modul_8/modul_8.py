# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# from datetime import datetime

# date='2024-10-09'

# def get_days_from_today(date):
#     year, month, day = map(int, date.split('-'))
#     # print(year,month,day)
#     date_user=datetime(year,month,day)
#     date_user=date_user.date()
#     # print("date_user:",date_user)
#     today=datetime.today()
#     today=today.date()
#     # print("Today is ",today)
#     delta_date=today-date_user
#     delta_date=delta_date.days
#     # print("delta_date:", delta_date)
#     return delta_date

# print(get_days_from_today(date))


# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# from datetime import datetime

# month=2
# year=2004

# def get_days_in_month(month, year):
#     month_d=0
#     a=year%4
#     if month == 2:
#         if a == 0:
#             month_d=29
#         else:
#             month_d=28
#     elif month in {4, 6, 9, 11}:
#         month_d=30
#     else:
#         month_d=31

#     return month_d

# print(get_days_in_month(month,year))


# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# from datetime import datetime
# date='2024-3-4 17:08:34.149Z'

# def get_str_date(date):
#     date_new, *args=date.split(" ")
#     year, month, day = map(int, date_new.split('-'))
#     # print(year,month,day)
#     date_user=datetime(year,month,day)
#     date_user=date_user.strftime('%A %d %B %Y')
#     # print(date_user)
#     return date_user
# print(get_str_date(date))


# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# import random
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
# quantity=2

# def get_random_winners(quantity, participants):
#     user_list=list(participants.keys())
#     # print(user_list)
#     random.shuffle(user_list)
#     # print(user_list)
#     len_user_list=len(user_list)
#     # print(len_user_list)
#     if quantity<=len_user_list:
#         win_user=random.sample(user_list,k=quantity)
#     else: win_user=[]
#     # print(win_user)
#     return win_user

# print(get_random_winners(quantity,participants))


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework


# from decimal import Decimal, getcontext

# number_list=[3, 5, 77, 23, 1.33543546]
# signs_count=6

# def decimal_average(number_list, signs_count):
#     getcontext().prec=signs_count
#     count=Decimal(0)
#     n=Decimal(len(number_list))
#     for i in number_list:
        
#         count=count+Decimal(i)
    
#     avrg=count/n
#     # print(avrg)
#     return avrg

# print(decimal_average(number_list, signs_count))

# getcontext().prec = 6
# print(Decimal(15) / Decimal(7))  # Decimal('0.142857'))

# getcontext().prec = 28
# print(Decimal(1) / Decimal(7))


# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# import collections

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
# cats1=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# cats2=[
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
# cats3=[1,2,3,4,5]

# cats=cats2


# def convert_list(cats):
#     a=cats[1]
#     print(a)
#     print("cats is list -",isinstance(cats,list))
#     if isinstance(a,tuple):
#         print("a is tuple -", isinstance(a,tuple))
#         res_list=[]
#         for cat in cats:
#             cat_dict={
#                 "nickname":cat.nickname,
#                 "age":cat.age,
#                 "owner":cat.owner,
#             }
#             res_list.append(cat_dict)
#         # print (res_list)
#     elif isinstance(a,dict):
#         print("a is dict -", isinstance(a,dict))
#         res_list=[]
#         for cat in cats:
#             # Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#             cat_list=Cat(cat["nickname"],cat["age"], cat["owner"])
#             # cat_list=Cat(**cat)._replace()
#             # print(cat["nickname"])
#             # print(cat["age"])
#             # print(cat["owner"])
#             # print(tuple(cat_list))
#             # print((cat_list))
#             res_list.append(cat_list)
#             # print(cat_list.nickname)
#         # print(res_list)
#     else: 
#         print ("cats does not have list or dict" )
#         res_list=[]
#     return res_list


# print(convert_list(cats))


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# from collections import Counter

# ips = [
#     "85.157.172.253",
#     "85.157.172.253",
#     "85.157.173.254",
#     "85.157.172.253",
#     "85.151.172.253",
#     "81.157.172.253",
#     "85.157.172.255",
#     "85.157.172.255",
#     "85.157.172.253",
#     "85.157.173.253",
# ]

# def get_count_visits_from_ip(ips):
#     ip_count=Counter(ips)
#     # print(ip_count)
#     return ip_count

# def get_frequent_visit_from_ip(ips):
#     ip_count=Counter(ips)
#     print(ip_count)
#     ip_max=max(ip_count, key=ip_count.get)
#     count_most=(ip_max,ip_count[ip_max])
#     print(ip_max)
#     print(count_most)
#     return count_most

# get_frequent_visit_from_ip(ips)


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
