
# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         return f'Hello! I am {self.name}'


# bill = Human('Bill')
# print(bill.say_hello())  # Hello! I am Bill
# print(bill.age)  # 0

# -----> Homework

# class Point:
#     def __init__(self,x, y):
#         self.x=x
#         self.y=y


# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10
        

# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory

# class PositiveNumber:
#     def __init__(self):
#         self.__value = None

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, new_value):
#         if new_value > 0:
#             self.__value = new_value
#         else:
#             print('Only numbers greater zero accepted')


# p = PositiveNumber()
# p.value = 1
# print(p.value)  # 1
# p.value = -1  # Only numbers greater zero accepted
# p._PositiveNumber__value = -1
# print(p.value)  # -1

# -----> Homework
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__x = None
#         self.__y = None
    
#     @property
#     def get_x (self):
#         return self.__x
    
#     @property
#     def get_y(self):
#         return self.__y
    
#     @get_x.setter
#     def get_x(self, new_x):
#         if new_x > 0:
#             self.__x=new_x
#         else:
#             print('Only numbers greater zero accepted')
    
#     @get_y.setter
#     def get_y(self, new_y):
#         if new_y > 0:
#             self.__y=new_y
#         else:
#             print('Only numbers greater zero accepted')

# point = Point(3, 3)

# print(point.get_x)  # 5
# print(point.get_y)  # 10

# point.get_x=-2
# print(point.get_x)

# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         if isinstance(x, int or float):
#             self.x = x
#         else: self.x=None

#         if isinstance(y, int or float):
#             self.y = y
#         else: self.y=None

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         # if isinstance(x, int or float):
#         if type(x) in (int, float):
#             self.__x=x
#         else:
#             self.__x=None
    
#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if type(y) in (int, float):
#         # if isinstance(y, int or float):
#             self.__y=y
#         else:
#             self.__y=None

# point = Point("a", 10)

# print(point.x)  # 5
# print(point.y)  # 10

# print(point.get_x)  # 5
# print(point.get_y)  # 10

# point.get_x=-2
# print(point.get_x)

# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         elif index ==1:
#             return self.coordinates.y
#         else:
#             print ("Індекс має бути 0 або 1")

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         elif index == 1:
#             self.coordinates.y=value
#         else: 
#             print ("Індекс має бути 0 або 1")



# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# vector[1] = 23  # Встановлюємо координату x вектора 10

# print(vector[0])  # 10
# print(vector[1])  # 10


# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f'Point({self.x},{self.y})'
        


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#         return f'Vector({self.coordinates.x},{self.coordinates.y})'


# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)

# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value == None:
#             return (self.coordinates.x,self.coordinates.y)
#         elif value>0:
#             return (self.coordinates.x*value,self.coordinates.y*value)
        
 
#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# vector = Vector(Point(1, 10))

# print(vector())  # (1, 10)
# print(vector(5))  # (5, 50)


# *********************<<<<<<< Homework 7 >>>>>>>>>>****************
# -------> theory
# from collections import UserDict


# class MyDict(UserDict):
#     def __add__(self, other):
#         self.data.update(other)
#         return self

#     def __sub__(self, other):
#         for key in other:
#             if key in other:
#                 self.data.pop(key)
#         return self


# d1 = MyDict({1: 'a', 2: 'b'})
# d2 = MyDict({3: 'c', 4: 'd'})
# d_n=MyDict({"x":"y"})

# # *******variant 1*********************************
# d4=d_n+d1+d2
# print(d4) #{'x': 'y', 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# d5 = d4 - d1
# print(d5)  # {'x': 'y', 3: 'c', 4: 'd'} - віднялось лише d1, d2 на місці

# #*********variant 2*******************************
# print("")
# d3 = d1 + d2
# print(d3)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# d4=d_n+d3 #по факту d4=d_n+d1+d2 чи не так?
# print(d4) #{'x': 'y', 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# d5 = d4 - d1 
# print(d5)  # {'x': 'y'} - чому такий результат? де ділось d2? я очікував, що буде як у варіанті 1, тобто {'x': 'y', 3: 'c', 4: 'd'}


# -----> Homework

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x,y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x,y))

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# vector3 = vector2 + vector1
# vector4 = vector2 - vector1

# print(vector3)  # Vector(11,20)
# print(vector4)  # Vector(9,0)


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         x= self.coordinates.x * vector.coordinates.x
#         y = self.coordinates.y * vector.coordinates.y 
#         return x+y
        

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# scalar = vector2 * vector1

# print(scalar)  # 110


# *********************<<<<<<< Homework 9 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         len_vect=(self.coordinates.x**2 + self.coordinates.y**2)**0.5
#         return len_vect
        

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# print(vector1.len())  # 10.04987562112089
# print(vector2.len())  # 14.142135623730951


# *********************<<<<<<< Homework 10 >>>>>>>>>>****************
# -------> theory
# -----> Homework


# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

#     def __eq__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1==len2


#     def __ne__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1!=len2

#     def __lt__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1<len2
        

#     def __gt__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1>len2
        

#     def __le__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1<=len2

#     def __ge__(self, vector):
#         len1=(self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5 # len firast vector
#         len2=(vector.coordinates.x ** 2 + vector.coordinates.y ** 2) ** 0.5 # len second vecotr
#         # print(len1, len2)
#         return len1>=len2
        


# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(3, 10))

# print(vector1 == vector2)  # False
# print(vector1 != vector2)  # True
# print(vector1 > vector2)  # False
# print(vector1 < vector2)  # True
# print(vector1 >= vector2)  # False
# print(vector1 <= vector2)  # True



# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework