import random

name_string = input("Give me everybody's names, separated by a comma.")
names = name_string.split(', ')

number_of_people = len(names)
who_pays = names[random.randint(0, number_of_people - 1)]
print(who_pays)

# this can be done with a python function
print(random.choice(names))