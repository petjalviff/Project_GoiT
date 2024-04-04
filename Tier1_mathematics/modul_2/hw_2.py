# import numpy as np

# # A=np.array([[4,2],[3,4]])
# # det_A=np.linalg.det(A)
# # print(round(det_A))

# B=np.array(
#     [[4, 11, 5, 4],
#      [6, 1, 3, -1],
#      [1, 2, 2, 1],
#      [1, 9, 5, -1],
#      ])
# det_B=np.linalg.det(B)


# Bt=np.transpose(B)
# det_Bt=round(np.linalg.det(Bt))

# print(B)
# print()
# print(Bt)
# print()

# print("det_B =",round(det_B))
# print("det_Bt =", det_Bt)


# *********************<<<<<<< Homework 2.1 and 2.2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

import numpy as np

A=np.array(
    [[-1,1,2],
     [0, -1, -3],
     [4, -3, 2],
    ])
B=np.array([1,-4,7])
res=np.linalg.solve(A,B)
# print(res)
a=A
b=B
def solve_cramer (a,b):
    n=len(b)
    # print(n)
    x=np.zeros(n)
    # print(x)
    det_a=np.linalg.det(a)
    # print(det_a)
    for i in range(n):
        a_i=a.copy()
        a_i[:,i]=B
        x[i]=np.linalg.det(a_i)/det_a
        # print(x)
    return x
print (solve_cramer(A,B))
