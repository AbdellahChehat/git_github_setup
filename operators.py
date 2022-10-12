

#a = 24
#b = 16

#print(a + b)
#print(a - b)
#print(a > b)
# #print(a < b) #
# ##print(a == b) #False
#
# # % find out what it is how to use it create print statement
#
#
# # The not-equal-to operator ( != ) returns true if the operands don't have the same value; otherwise, it returns false
#
# ###a = 12
# ####b = 13
#
# #####print (a != b )
#
#
# #greeting = "Hello world!"
#
# #print(greeting)
# #print(greeting.isalpha())
# #print(greeting.islower())
# #print(greeting.startswith("H"))
# #print(greeting.endswith("!"))
# #print(greeting.isdigit())
#
# # -----------------------------------------------------
# # String Slicing you need to index []
#
# # String indexing  - strats from 0
#
# # greeting = "Hello world!"
# #
# # print(greeting)
# # # check length
# # print(len(greeting))
# #
# # # String Slicing
# # print(greeting[0:5])
# # print(greeting[6:12])
#
# # ----------------------------------------
#
# # String Methods are available
#
#
# white_space = "lot's of spaces at the end                    "
# print(len(white_space))
#
# # Strip() removes white spaces at the end of the string
# print(len(white_space.strip()))
#
# #Count functions tells you how many times a certain number, letter or string appears
# example_text = "Here's some text with lot's of text"
# print(example_text.count("text"))
# print(example_text.upper())
#
# example_text1 = "Here's sOme text with lOt's of text"
# print(example_text1.lower())
# #Replaces a word
# print(example_text.replace("with", "suii"))
#
#
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


