# print the average of 3 numbers.
print("enter only 3 numbers")
a = int(input("enter a number"))
b = int(input("enter another number"))
c = int(input("again enter a number"))
def average():
    avg = (a + b + c)/3
    print("the average of 3 numbers is",avg)
average()  

# write a function to print the length of a list

list1 = [1,2,3,4,5,6]
def list_len(list):
    print(len(list))
list_len(list1) 


#write a function to print the element of a list in a single line

cities=["Delhi","BBSR","Goa","Mumbai","Pune"]

def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end =" ")
print_list(cities)


# write  a function to find the factorial of n.

n = int(input("enter a number"))
def factorial():
    i = 1
    fact = 1
    while(i<=n): #for i in range(1,n+1)
        fact = fact * i
        i = i + 1
    print("the factorial of this number is",fact)
factorial()   

# write a function to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"dollar is",inr_val,"rupees")
converter(5)    
