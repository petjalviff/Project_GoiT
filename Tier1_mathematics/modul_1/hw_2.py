import numpy as np

# A=np.array([[4,2],[3,4]])
# det_A=np.linalg.det(A)
# print(round(det_A))

B=np.array(
    [[4, 11, 5, 4],
     [6, 1, 3, -1],
     [1, 2, 2, 1],
     [1, 9, 5, -1],
     ])
det_B=np.linalg.det(B)


Bt=np.transpose(B)
det_Bt=round(np.linalg.det(Bt))

print(B)
print()
print(Bt)
print()

print("det_B =",round(det_B))
print("det_Bt =", det_Bt)


