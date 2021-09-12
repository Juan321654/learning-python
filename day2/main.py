import math
# num_char = len(input("what is your name?"))

# print("your name has " + (str(num_char) + " Characters"))

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(math.floor(weight / height**2))

# f-String
name = "juan"
last_name = "camacho"
print(f"first name: {name}, and last name: {last_name}")

age = 90 - int(input("What is your current age?"))
days = age * 365
weeks = age * 52
months = age * 12

print(f"You have {days} days, {weeks} weeks, {months} months left")