# example of abstarction

class car:
    # parameterised constrcter
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = car()
car1.start()    


 
#example of encapsulation

class student:
    def __init__(self,name = "pinku",marks = 80):
        self.name = name
        self. marks = marks 
s1 = student()
s2 = student("asish",78)

print("name:{} marks:{}".format(s1.name,s1.marks))
print("name:{} marks:{}".format(s2.name,s2.marks))