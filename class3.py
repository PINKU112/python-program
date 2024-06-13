str1 = "this is good day"
str2 = 'this is beautiful day'
str3 = """this is a bad day"""

gift = "this is good day and will \n sleep whole day in my room."
print(gift)


# string concatination ->

str1 = "web"
str2 = "bocket"
print(str1 + str2)

str3 = "dinabandhu"
str4 = "nayak"
print(str3 + str4)


# length of string ->

str1 = "web bocket"
len1 = len(str1)
print(len1)

str2 = "webbocket"
print(len(str2))


str1 = "web"
str2 = "bocket"
str3 = str1 + " " + str2
print(str3)
print(len(str3))


# indexing of string ->

str = "gandhi institute of excllent technocarts"
print(str[1])
print(str[6])
print(str[13])

# slicing of string ->

str = "webbocket"
print(str[1:4])
str = "gietcollege"
print(str[4:])
print(str[:4])


# function of string ->
# str.endswith()

str = "i am student of GIET college. GIET is best college, GIET is the only one best cin odisha"
print(str.endswith("odisha"))
print(str.endswith("sha"))
print(str.endswith("GIET"))

# str.capitalize()

print(str.capitalize()) # first letter of the first word should be capital.

# str.replace()

print(str.replace("GIET","GEC"))
print(str.replace("a","20"))

# str.find()

print(str.find("GIET"))

# str.count()

print(str.count("GIET"))