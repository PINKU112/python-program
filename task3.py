# write a program to check if a number entered by a user is even or odd

num = int(input("Enter a number:"))
if(num % 2 == 0):
    print("the number is an even number.")
else:
    print("the number is an odd number.")


# write a program to find the greatest of three numbers entered by the users

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if(num1 >= num2 and num1 >= num3):
    greatest = num1
elif(num2 >= num1 and num2 >= num3):
    greatest = num2
else:
    greatest = num3
print("the greatest number is:",greatest)


# write a program to check if a number is multiple of 7 or not

num = int(input("Enter a number:"))
if(num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")