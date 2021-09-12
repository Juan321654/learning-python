# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#   print("You can ride")
# else: 
#   print('Sorry, you cant')

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#   print('its even')
# else:
#   print('Its odd')

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ").lower()
# add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N ").lower()

# bill = 0
# if size == "s":
#   bill += 15
# if size == "m":
#   bill += 20
# if size == "l":
#   bill += 25
# if size == "s" and add_pepperoni == "y":
#   bill += 2
# if size == "m" or size == "l" and add_pepperoni == "y":
#   bill += 3
# if extra_cheese == "y":
#   bill += 1

# print(f"Your final bill is: ${bill}")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

total = 0
total += name1.count("t") + name2.count("t")
total += name1.count("r") + name1.count("r")
total += name1.count("u") + name1.count("u")
total += name1.count("e") + name1.count("e")

print(total)