# Python Intro

### Why Python ?


- Mature and Supportive Python Community
-  Support from Renowned Corporate Sponsors
- Versatility, Efficiency, Reliability, and Speed
- Easy to learn


### Python Use cases
![](../../Desktop/python-use-cases-7.jpg)

### Python Variables 

- Below I've listed some of the python variables we covered during our class.

1. Integer = Int = 32
2. Boolean = Bool = True or False 
3. Float = 1.34 
4. String = "Abdellah"



``` Python
# Testing
# Dynamically typed language
# Python Variables
# TO store Any data
# To store user data - hard code the data - any other type
# first_name = "Angel" - string
# DOB = 99 = int
# uk_resident = yes or No = Boolean
# travel = 14.5 - float
# type = find out type of data

#first_name = "Abdellah"
#last_name = "Chehat"



#print (first_name)


#print("Good morning, Please enter Your Name ")

#name = input()
#print(name)

#print("Hello dear " + name)

#
print("Good Morning, Please enter your First Name")
first_name = input()
#
print ("Enter Last Name")
last_name = input()
#
print("Enter DOB")
DOB = input()

print("Are you a Uk resident? Answer Yes or No")

uk_resident = input()


print(f'Hello   {first_name}  {last_name}')
print (DOB)
print (uk_resident)

```


------------

## How to generate a new SSH Key:
 
1.     Open terminal 
 
2.     Paste ssh-keygen -t ed25519 -C apedros@spartaglobal.com

<img width="730" alt="Screenshot 2022-10-11 at 09 39 21" src="https://user-images.githubusercontent.com/115224560/195042103-c2b0b2db-b514-4461-968f-0f944438a3b5.png">
 
3.     Click enter till it’s done 
 
4.     Type “ls” into terminal to find the ssh key created 
 
5.     Find the public key created 
 
6.     cat “public key” 
 
7.     copy the key 
 
8.     Open github click on account>settings> SSH and GPC keys 
 
9.     Create a new SSH key 

10.     Once completed you’ll need to push work onto gitHub
 
 
## How to push work onto GitHub
 
 
1.     Save work of Pycharm 
2.     Open terminal on Pycharm
3.     First command (git init)
4.     Followed by git status (optional)
5.     git add . 
6.     git commit -m “update”
7.     git push -u origin main


## Diagram
<img width="549" alt="Screenshot 2022-10-10 at 17 26 17" src="https://user-images.githubusercontent.com/115224560/194913067-057a52f9-b198-4fdf-936d-c2d4758d6b1e.png">

#### Git & Github 
- add changes to our Git-Hub repo - the changes that we made 

- `git add filename` or `git add .` means push everything
- ``git commit -m "Update" ``  provides  a message 
- `git push -u origin main` now lets send this new data to github 

- Comment is control / 

## String Slicing

```` python

# String Slicing you need to index []

# String indexing  - strats from 0

greeting = "Hello world!"
#
# print(greeting)
# # check length
# print(len(greeting))
#
# # String Slicing
# print(greeting[0:5])
# print(greeting[6:12])

````

## Operators 

```` python
#a = 24
#b = 16

# Mathematical

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#print(a > b)
#print(a < b) #
##print(a == b) #False

# % find out what it is how to use it create print statement


# The not-equal-to operator ( != ) returns true if the operands don't have the same value; otherwise, it returns false

#a = 12
#b = 13

#print (a != b )


#greeting = "Hello world!"

#print(greeting)
#print(greeting.isalpha())
#print(greeting.islower())
#print(greeting.startswith("H"))
#print(greeting.endswith("!"))
#print(greeting.isdigit())

````

## String Methods 
```` python

# String Methods are available


white_space = "lot's of spaces at the end                    "
print(len(white_space))

# Strip() removes white spaces at the end of the string
print(len(white_space.strip()))

#Count functions tells you how many times a certain number, letter or string appears
example_text = "Here's some text with lot's of text"
print(example_text.count("text"))
print(example_text.upper())

example_text1 = "Here's sOme text with lOt's of text"
print(example_text1.lower())
#Replaces a word 
print(example_text.replace("with", "suii"))



````
### Concatenation and   casting

```` python

# # Concatenation and   casting
#
# # user data input

first_name = "Abdellah"
last_name = "Chehat"
salary = 40
salary1 = "40"

print(first_name)
print(last_name)

print(first_name + " " + last_name + "" + salary1)

# combining differnt data type in one print function 
print(first_name + " " + last_name , salary)
# f string can combine different data types in a line 
print(f'{first_name} {last_name} {salary1}')


````

Data collections

```` python
#Data collections
# List
# Tuples
# Dict

# Lists, synatx ["sdsda" , "sdasd" ]

shopping_list = ["ketchup", "fanta", "apple", "bread"]

# In order to add an item to the list at the end of the list we use ".append"
shopping_list.append("banana")

# In order to replace an item you need to know the index of the item you are replacing and then add the new item e.g below
shopping_list [0] = "jam"

# In order to remove items from a list
shopping_list.remove("fanta")

#removes last item of a list by using pop

shopping_list.pop()


print(shopping_list)
print(type(shopping_list))



# list can have multiple data types

multi_list = [1,2,3, "string", "apple"]

# Tuples
# Immutable - can't be (changed - edited - added)
# Tuples syntax (")

essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))


# what is the difference between lists and tuples


````



User Task 1:

```` python
#
print("Good Morning, Please enter your First Name")
first_name = input()
#
print ("Enter Last Name")
last_name = input()
#
print("Enter DOB (Format dd/mm/yyyy")
DOB = input()

print("Are you a Uk resident? Answer Yes or No")

uk_resident = input()

print("Enter First line of address")

first_line = input()

print ("Enter second line of address")

second_line = input()

print ("Enter postcode (Format N1 1TB)")

postcode = input()


print ("Enter Favourite hobby")

hobby = input()



print(f'Hello, {first_name.capitalize()} {last_name.capitalize()} Your date of birth is {DOB} and you are {uk_resident} uk resident')
print(f'Your address is {first_line} {second_line} {postcode}')
print(f'Your favourite hobby is {hobby.lower()}')

````