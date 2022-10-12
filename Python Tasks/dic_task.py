
# 1 Define a dic called story1

story1 = {
    "start":"Once upon a time there lived 3 little piggies. They all lived together in the woods",
    "middle": "One dark cold night one of the piggies went out for a walk by himself, not knowing that a pack of wolves had recently moved moved into the woods near by",
    "end":"Unfortunately two wolves spotted him and started to chase him. He run and run and run but it wasn't good enough. The poor little piggy was caught and eaten by the wolves",

}
# ##2 - Print the entire dictionary
#
# print(story1)
#
# #3 - Print the type of your dictionary
#
# print(type(story1))
#
# #4 - Print only the keys
# print(story1.keys())
#
# #5 - print only the values
#
# print(story1.values())
#
# #6 - print the individual values using the keys (individually, lots of printi commands)
# print(story1["start"])
# print(story1["middle"])
# print(story1["end"])

#7 - Now let's add a new key:value pair. -  'hero': yourSuperHero


story1["hero"] = "Daddy pig"
print(story1)