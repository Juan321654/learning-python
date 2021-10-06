import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
# .items() = Object.entries()
passed_students = {student:grade for (student, grade) in student_scores.items() if grade >= 60}

print(passed_students)