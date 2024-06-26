

# print the element of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

# search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter a number"))
i = 0
for val in tup:
    print(val)
    if(val == x):
        print("number found at index",i)
        i = i + 1 

