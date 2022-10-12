# What is a dictionary
# How to manage Dic - How to Manage the data using dict
# It works as key Value pair key = value
# Syntax { "Key" : "Value" }


# Store students data - name, stream, progress, completed_lessons

student_1 = {
    "keys": "values",
    "name": "Abdellah",
    "stream": "devops",
    "completed_lesson" : 4 ,
    "completed_lesson_names": ["tuples","lists","strings"]

             }
#print(student_1)
#print(type(student_1))

print(student_1["stream"]) #This will display the value saved inside the stream

# Questions 1 print/dispaly completed_lessons_names

print(student_1["completed_lesson_names"])

# Questions 2: print/display completed_lessons_names index 0
print(student_1["completed_lesson_names"][0])


#How to change a keys value
student_1["completed_lesson"] = 3
print(student_1["completed_lesson"])

#how to remove items from a key in a dic
student_1["completed_lesson_names"].remove("strings")

print(student_1)

# Dict Built in methods

# Display keys only or values
# keys() values()
print(student_1.keys())

#Dispaly values only from student_1
print((student_1.values()))

