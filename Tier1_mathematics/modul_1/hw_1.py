# # import numpy as np
# # a=np.array([[1, 2, 3, 4, 5]])
# # b=np.array([[1/2, 1, 2, 3, 4]])
# # res=a+b
# # print(res)

# # b_trans=b.T
# # print()
# # print (b_trans)
# # print("*"*20)
# # print(a)
# # print()
# # print(b_trans)
# # c=a+b_trans
# # print()
# # print(c)

# # d=np.dot(a, b_trans)
# # print()
# # print("d:",d)
# # print("*"*20)
# # print(a)
# # print(b)
# # e=a/b
# # print(e)
# # print("*"*20)
# # f=a/b.T
# # print(a)
# # print(b_trans)
# # print(f)

# # *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# # -------> theory
# # -----> Homework

# import numpy as np


# M5=np.array([[0.866, -0.5],[0.5, 0.866]])
# # print(M1)
# M4=np.array([[1, 0],[1.732, 1]])
# M2=np.array([[-1,0],[0,-1]])
# M1=np.array([[0.5,0],[0,3]])

# print(M4)
# print()
# print(M2)
# print()
# print(M1)
# M6=M5*M4*M2*M1
# print()
# print(M6)
# m6d=np.dot(np.dot(np.dot(M5,M4),M2),M1)
# print()
# print(m6d)


# x=np.array([[2],[1]])
# M6x=np.dot(m6d,x)
# print()
# print(M6x)
