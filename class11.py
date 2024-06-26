

# example of private attributes and methods

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
    def reset_pass(self):
        print(self.acc_pass)    
acc1 = account("12345","abcde")        
print(acc1.acc_no)
print(acc1.reset_pass())


class Person:
    __name = "rohit" #private attributes

    def __hello(self): #private method
        print("hello person!")

    def welcome(self): #a method to pass our private method
        self.__hello()

p1 = Person()
print(p1.welcome())

# example of single inheritance

class car:
    @staticmethod #decorator
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")
class toyotacar(car):
    def __init__(self,name):
        self.name = name
car1 = toyotacar("fortuner")
car2 = toyotacar("legender")
print(car1.stop())
print(car2.start())                    



