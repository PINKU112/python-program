name = "shradha"
age = 25
salary = 23000.00
onTime = False
a = None

print(type(name))
print(type(age))
print(type(salary))
print(type(onTime))
print(type(a))

# comments -
# single line comment

"""
today is a day 
we just learn python 
do some code etc...
"""

# print a sum of two numbers
a = 10
b = 20
sum = (a+b)
print("my total sum is:",sum)

# operator -
# arithmatic operator

a = 5
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#relational operator

a = 50
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

#assignment operator 

num = 10
num = num + 10

print("num: ",num)

#logical operator


val1 = True
val2 = False
print("AND operator: ", val1 and val2) #it takes both val1 and val2 - false
print("OR operator: ", val1 or val2) #either it take val1 or val2 - true

# true + true = true
# true + false = false
# false + false = false
# false + true = false

#input

name = str(input("enter your name: "))
value = int(input("enter your age: "))
mySalary = float(input("enter your salary: "))

print("welcome ",name)
print("my age is ",value)
print("my salary is ",salary)