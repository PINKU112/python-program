

class Student:
    name ="web bocket"
s1=Student()
print(s1) # memory location where our s1 object will stored.
print(s1.name) # web bocket



class Car:
    color = "blue"
    brand = "Toyota"
car1=Car()
print(car1.color) # blue
print(car1.brand) # Toyota
      # or
print(car1.color,car1.brand)


# init function..............


class Student:
    def _init_(self,fullname):
        self.name = fullname
        print("we can add a student in our Database")

s1 = Student("web bocket")
print(s1.name) # web bocket

s2 = Student("Software")
print(s2.name) # Software


class Student:
    #default Contructor
    def _init_(self) -> None:
        pass

    #parameterized Constructor

def _init_(self,name,marks):
    self.name = name
    self.marks = marks
    print("adding new student to the database..")

s1 = Student("web bocket",89)
print(s1.name, s1.marks)

s2 = Student("software",98)
print(s2.name, s2.marks)


# class and instance...


class Student:

    college_name = "ABC college"
    name= "anonymous" #class Attributes

    def _init_(self,name,marks):
        self.name = name # object attributes > class attributes..
        self.marks = marks
        print("adding new student to the database..")

s1 = Student("rohan",98)
print(s1.name) # rohan



# example of method..........

class Student:
    def _init_(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        print("your mark is",self.marks)

s1 = Student("rohan",98)
s1.welcome()
s1.get_marks()
