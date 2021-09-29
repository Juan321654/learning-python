programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
# print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The definition of a loop"
# print(programming_dictionary)

# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

user_roles = {}
user_roles["Juan"] = "Programmer"
user_roles["Tim"] = "Boss"
user_roles["Dave"] = "Sales man"

print(user_roles)

names = []
names.append({"Juan": 30})
names.append({"Steph": 60})

print(names)

user_roles["Juan"] = "what"

print(user_roles)