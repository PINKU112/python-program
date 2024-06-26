# print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i = i + 1


# print number from 100 to 1.

i = 100
while i >= 1:
    print(i)
    i = i -1


# print the multiplication table of number n.

a = int(input("enter a number"))
i = 1
while i <= 10:
     print(a,"*",i,"=",a * i)
     i = i + 1

# print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]

i = 1
while i <= 10:
    a = i * i
    print(a)
    i = i + 1     
         

# search for a number x in this tuple using loop 
#(1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter a number"))
i = 0
while i < len(tup): 
    if(tup[i] == x):
        print("found at index",i)
    else:
        print("finding...") 
    i = i + 1
