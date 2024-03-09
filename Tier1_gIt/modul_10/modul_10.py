# *********************<<<<<<< Homework 1 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     animal_name=""
# animal=Animal()

# *********************<<<<<<< Homework 2 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname=nickname
#         self.weight=weight
    
#     def say(self):
#         pass



# animal=Animal("Boris",10)

# print(animal.nickname)
# print(animal.weight)

# *********************<<<<<<< Homework 3 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname=nickname
#         self.weight=weight
    
#     def say(self):
#         pass
    
#     def change_weight(self, weight_new):
#         self.weight=weight_new


# animal=Animal("Simon",10)

# print(animal.nickname)
# print(animal.weight)
# animal.change_weight(12)
# print(animal.weight)

# *********************<<<<<<< Homework 4 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
    
#     def change_color(self, color_new):
#         self.color=color_new


# first_animal=Animal("Simon",10)
# second_animal=Animal("Vaska",9)


# first_animal.change_color("red")
# print(first_animal.color)
# print(second_animal.color)

# *********************<<<<<<< Homework 5 >>>>>>>>>>****************
# -------> theory
# -----> Homework

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"
    

# cat=Cat("Simon", 10)

# print(cat.say())


# *********************<<<<<<< Homework 6 >>>>>>>>>>****************
# -------> theory
# -----> Homework

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed=breed
        
    def say(self):
        return "Woof"
    

dog = Dog("Barbos", 23, "labrador")

print(dog.nickname)
print(dog.weight)
print(dog.breed)
print(dog.say())


# *********************<<<<<<< Homework 8 >>>>>>>>>>****************
# -------> theory
# -----> Homework