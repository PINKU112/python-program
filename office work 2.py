# print numbers from 1 to 100.

for i in range(1,101):
    print(i)

# print numbers from 100 to 1. 

for i in range(100,0,-1):
    print(i)  

# print the multiplication table of  a number n.

n = int(input("enter a number"))
for i in range(1,11):
    print(n,"*",i,"=",n * i)