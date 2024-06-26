

# wrte a program to print hello world in 5 times.

count = 1
while count <= 5:
    print("hello world")
    count = count + 1

# print the numbers from 1 to 5.

i = 1
while i <= 5:
    print(i)
    i = i + 1

# print the numbers 5 to 1.

i = 5
while i>= 1:
    print(i)
    i = i - 1

# break example

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i = i + 1

# continue example


i = 0
while i <= 5:  
    if(i == 3):
        i = i + 1
        continue
    print(i)
    i = i + 1


# example of FOR loop.

nums = [1,2,3,4,5,6,7]
for i in nums:
    print(i)

cars = ["BMW","GWAGON","MARUTI","THAR","COMPAS"]
for val in cars:
    print(val)

str = "webbocket"
for c in str:
    print(c)    

    
        

