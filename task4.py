

# write a program to ask the user to enter names of their 3 favorite movies and store them in a list.list.list.      


print("enter names of your 3 favorite movies")
movie1 = str(input("enter your 1st movie name"))
movie2 = str(input("enter your 2nd movie name"))
movie3 = str(input("enter your 3rd movie name"))
list = [movie1 , movie2 ,movie3]
print(list)


# write a program if a list contains a palindrome of elements.

print("enter a list which has 3 elements")
a = int(input("enter a number"))
b = int(input("enter another number"))
c = int(input("enter another number"))
list1 = [a,b,c]
print("the original list is",list1)
rev1 = list1 [:: -1]
res1 = rev1 == list1
print("is the list palindrome ",res1)
 

 # write a program to count  number of students with the "A" grade in the following tuples.
 #  ex. ("c","D","A","A","B","B","A").store the above value in alist & sort them from "a" to "D".
 
tup1 = ("c","D","A","A","B","B","A")
print(tup1.count("A"))
list1 = ["C","D","A","A","B","B","A"] 
print("the present list is:",list1)
list1.sort()
print(list1)