# Python Intro
- Why Python
- Python Use cases
- Python Set Up with Pycharm
- Python Variables 


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




