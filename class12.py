

# # example of multiple inheritance.

# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB) 
# print(c1.varA)           


# # example of multilevel inheritance

# class Car:
#     @staticmethod # decorator
#     def start():
#         print("car started...")

#     @staticmethod # decorator
#     def stop():
#         print("car stoped...")

# class ToyotaCar(Car):
#     def _init_(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def _init_(self,type):
#         self.type = type

# car1 = Fortuner("disel")
# car1.start()

# example of polymorphism


class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,newImg)

num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1 + num2 
# num3 = num1.add(num2)
num3.showNumber()