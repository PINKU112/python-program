# example to apply a condition for licence.

age = int(input("enter your age:"))

if(age >= 18):
    print("can apply the licence")
else:
    print("you can't apply for licence")


#example of traffic lights.

light = input("enter the signal you see:")

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("you are fool")    


# example of student marksheet.

mark = float(input("enter your mark:"))

if(mark >= 90):
    grade = "A"
elif(mark >= 80 and mark < 90):
    grade = "B"
elif(mark >= 70 and mark < 80):
    grade = "C"
elif(mark >= 60 and mark < 70):
    grade = "D"
elif(mark >= 50 and mark < 60):
    grade = "E"
else:
    grade = "f -> sorry you are fail"   

print("grade of the student is:",grade)

# example of list.

list = [45, 67, 34, 90, 76, 32]
print(list)
print(type(list))
print(list[0])
print(list[1])
print(list[2])
print(len(list))

# example of list slicing.

marks = [23,25,67,78,98]
print(marks[1:4]) 
print(marks[:3]) 
print(marks[2:])

#example of list method.

list = [2,1,3]
list.append(5)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(1,4)
print(list)
list.remove(1)
print(list)
list.pop(3)
print(list)




