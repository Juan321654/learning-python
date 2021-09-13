# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Get the average height
# Example Input 156 178 165 171 187
# Exmaple output 171

#Write your code below this row 👇
total = 0
for height in student_heights:
  total += int(height)
print(total)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

# This is just how sum and len work unser the hood