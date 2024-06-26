what is python ?

- python is simple, easy and portable.
- python is free and open source.
- python is high level interpreted language.
- python is devloped by guido van rosum.


- python us interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language.

- print is function to give output statement in python. simply we can tell "print" is output function.

character set of python language :-
1. letter -> A-Z, a-z
2. digits -> 0-9
3. speical character -> -,+,*,/ etc.....
4. whitespace -> blank space,tab,newline

what is variable in python :- a variable is a name given to memory location in a program or else we can simply say variable is container to store some data.

example -
nmae="shradha"
age= 23
salary= 23000.56

variable - name,age,salary
variables - "shradha" , 23,23000.56


rules for identifiers :-
1. identifiers - name of the variables
2. identifiers can be combination of uppercase and lowercase letter, digits and an underscores(_). ex. myVariable , variable_1
3. an identifiers can not start with digits.so while variable1 is valid but 1variable is not valid.
4. we cann't use speical characters or sumbol like !,#,@,%,etc..
5. identifiers can be of any length.
6. variables name should be small and meaningful like - when we give our age in that case we take the variable as "myAge".
myAge -> camle case letter.


- 'type' is operator is show the datatypes anme in our variables like which datatypes we use in our variables.


DATATYPES :-
- mainly datatypes of 5 types in python.
- these data types are unmuteable or bulid-in data types .
1. integer - +ve value,0,-ve value.
2. string - "hello" , "shradha" , etc..
3. float - 0.46,4.00, etc...
4. boolean -true, false
5. none - not assign


comments in python :-
  

- when we can write some code but don't want to execute it then we give the comment line to that place so that line of code will not executed.
- comments are of 2 types 
1. single line comment -
   when we give the single line comments in python we did it on "#".
   ex.
   # single line comment
   # this is a comment
2. multi line comment -
when we give the multi line comment in python we did it through """_""".
ex. 
"""
  multi line 
  comments
  """

  types of operator :-
  - simply we can say operator is symbol tha performs a certain operations between operands.
  ex. a + b
  a,b -> operands
  + -> operators
- there are 4 types of operators present in python
1. arithmatic operator. - (+,-,*,/)
2. relational operator. - (==,!=,>,<,>,<=,>=)
3. assignment operator. - (=,+=,-=,*=,/=,%=) 
4. logical operator. - (and, or, not)

Input in python :-
 
 - Input() statement is used to accept values(use keyboard) from user.

strings :-
 
 - string is datatype that stores a sequence of characters.


 str1 = "this is good day"
 str2 = 'this is beautiful day'
 str3 = """this is a bad day"""

all these string are real string because in python it supports all os these syntax like - "",'',""" """

- \n(new line) - when we want break our line into a new line then we can give the the new line symbol in that place so the line get breaked automatically.

basic operation of strings :-

1. concatination ->
      "hello" + "world" =
2. length of string ->
      len(str)  


indexing of string ->

- webbocket -> 012345678(indexing)
- always indexing start from '0'.


slicing of string ->

- accessing a part of string.
- ending index is not counting.
- syntax - str[starting_index : ending_index]

str = "webbocket"
str[0:3] - web
str[:3] - web
str[3:] - bocket


function of string ->

ex -
str = "i am a coder"
1. str.endswith("er.") - returs true if staring ends with substrings.
2. str.capitalize() - returns 1st character is capital.
3. str.replace(old,new) - replace all occurrences of old with new.
4. str.find(word) - returns 1st index of 1st occurrence.
5. str.count("am") - counts the occurrence of substring in string.


conditional statement ->

- used to handle the condition in your progrm.
- syntax (if-elif-else)
- elif means else-if

if(condition):
   statement1
elseif(condition):
   statement2
else:
   statement(default)      



lists in python ->

- list is built in datatype that stores set of values.
- it can store elements of different types like integer, float & strings etc..
- in list we can make indexing.
- in list we can find the length of the list also.

ex -
marks = [87, 45, 67, 83, 45] - array and list
student = ["hitesh", 85, "bhubaneswar"] - list

list sliceing ->

- it similar to string slicing.
- syntax - list_name[starting_idx : ending_idx]
- ending index is not include.

marks = [23,25,67,78,98]
marks[1:4] -> [25,67,78]
marks[:3] -> [23,25,67]
marks[2:] -> [67,78,98]

list methods ->

list = [9,4,7,8,1]
list.append(6) - adds one element at the end of the list - [9,4,7,8,1,6]
list.sort() - sort the elements an assending order - [1,4,7,8,9]
list.sort(reverse=true) - sort the elements in decending order - [9,8,7,4,1]
list.reverse() - reversing the list - [1,8,7,4,9]
list.insert(idx,el) - insert the element an index.
list.remove(1) - remove the first occurrence of element - [9,7,8,4]
list.pop(idx) - remove element at index.

GIT :- 

- git is a open source repository system where we can save , mainuplate , colaborate our code with any one else.
- in our software era, everyone can use git system for their software devlopment.
- we also called git is a version control system.
- git provide some tools to use their functionality and features ex - github , gitlab etc...



tuple in python :-

- tuple is a bulid in data type that lets us create imutable (the value cannot be changeable) sequence of values.
- ex.tup = (87,67,98,34,45)
- tup[0] -> 87
- tup[1] -> 67
- we can do the tuple as 
1. tup1 = () -> empty tuple 
2. tup2 = (1,) -> a tuple 
3. tup3 = (34,67,89,20) -> tuple
- tuple has also satisfy the sliceing property.

tuple methods :-

- tup.index(element) -> return index of first occurrence  (it returns the element is placed which index number)
- tup.count(element) -> return the count total occurrence (count the 1 which are present in the tuple)

ex. tup = (2,1,3,1)
tup.index(1) -> 1
tup.count(1) -> 2 

dictionary in python :-

- dictionary are used to store the data values in key:value pair.
- they are unordered,mutble(changeable) & donot allow duplicate keys.
- ex.
dict = {
   "name" : "pinku",
   "cgpa" : 8.1,
   "marks" : [88,86,85],
}
- the left part of the dictionary are the keys and right side part in their values so dictionary contains key : value pair structure.


nested dictionary in python :-
 - dictionary also satisfy the nested proerty.
 - dictionary under dictionary is called nested dictionary.
 - ex.
 student = {
   "name" : "mithun",
   "score":{
      "chem" : 98,
      "math" : 87,
      "phy" : 79
   }
 }


 dictionary methods :-

 1. myDict.keys() - it returns all keys.
 2. myDict.values() - it return aal values.
 3. myDict.items() - it will retirn all key : value pair as tuple.
 4. myDict.get("key") - return the key according the values.
 5. myDict.update(newDict) - insert the specified items to the dictionary.


 set in python :-

 - set is the collection of unordered items.
 - each element in the set must be unique and immutable(cannot be change )
- ex.
nums = {1,2,3,4,5}
set2 = {5,8,9,4}
  
set methods :-

1. set.add(element) -> add an element.
2. set.remove(element) -> remove an elemnt.
3. set.clear() -> clear all elemnts.
4. set.pop() -> remove a random value of set.
5. set.union(set2) -> combine both set values and return a new set.
6.set.intersection(set2) -> combine the common values and return a new set.


ex.

set1 = {1,2,3,2,4}
set2 = {3,7,2,6,4}
set1.union(set2) -> {1,2,3,4,6,7}
set1.intersection(set2) -> {2,3,4}


loops in python :-


- loops are used to repeate instruction.
- in python there are 2 loops - while loop , for loop
1. while loop :-
syntax - 
intialization
while condition:
   statement
   increment/decrement.


Break & Continue :-

  - break: break is used to terminate the loop when encountered.
  - continue: terminates execution in the current iteration & continue execution of the loop with the next iteration.  


2. for loop :-

- for loop are used for sequential traversal. for traversing list, string, tuple etc..
- syntax :-
   for val in list:
    statements...


range() :-
- range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),and stops before a specified number.
- syntax -> range(start, stop, step)


function in python :-
- function is a block of statements that performs a specific task.
- syntax :-
def func_name(parameter 1 ,parameter2...)
some statement
returns val

func_name(arg1,arg2..) #function call



- function are of 2 types in python
1. built-in function - print(), len(), type(), range()...etc
2. user defined function - user can devlope the function.


Object oriented programming in python:-->

--To map with real world scenarios,we started using objects in code.  
--This is called object oriented programming(OOP).

1st concept:--> Procedural programming.
2nd concept:--> Functional programming.
3rd concept:--> Object oriented programming.

Class and Object in python:-->

--Class is a blueprint for creating objects.
ex:-->Creating a class .
class Student:
   name = "web bocket"

ex:-->creating a object(instance)
s1 = student()
print(s1.name)  #web bocket

___init___ Function(constructor):-->

--All class have a function called _init_(), which is always when the class is being initialised.

ex:--> creatinig a class 
class Student:
   def_init_(self,fullname)
     self.name=fullname

ex:-->creating a object
s1=Student("web bocket")
print(s1.name)

Note:-->The self parmeter is a referene to the current instance of the class and is used to access variable that belongs to the class.


Class and instance Attributes:-->

university --> college1,college2,college3,college4
               student1,student2,student3,student4

--colleges and students are the attributes of university.


Methods in python:-->
--Methods are function that belongs to objects.

ex:-->creating class
class Student:
  def_init_(self,fullname)
     self.name = fullname
  def hello(self):
     print("hello",self.name)

ex:-->creating object
s1 = Student("rohan")
s1.hello()

Abstraction :-
- hiding the implimentation details of a class and showing the essential fatures of the user.

Encapsulation :-
- wrapping data and a function into a single unit(object).


Private(like) Attributes & Methods :-
- private attributes & methods are ment to be used within the class and are not accessible from outside the class.
- the private class attributes are written in __(attributes) so that we call it private attributes of a class. 

Inheritance :-
- when one class derives some property and methods of another class .
- syntax :-
class car:
    ---------
class toyotacar(car):
    ---------
- in python inheritance are of 3 typs 
1. single inheeritance
2. multi-level inheritance
3. multiple inheritance   

Polymorphism : operator overloading :-

- when the same operator is allowed to have different meaning accordingly to the context.
- In that polymorphism we can use dunder functions.
1. a + b -> __add__
2. a - b -> __sub__
3. a * b -> __mul__
4. a / b -> __truediv__
5. a % b -> __mod__
  
ex - (+)
print(1 + 2) #3 (addition)
print("web" + "bocket") #web bocket (concatination)
print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6] (merged) 





