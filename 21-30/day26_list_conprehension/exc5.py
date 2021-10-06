weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# example output:
# {
# 'Monday': 53.6, 
# 'Tuesday': 57.2, 
# 'Wednesday': 59.0, 
# 'Thursday': 57.2, 
# 'Friday': 69.8, 
# 'Saturday': 71.6, 
# 'Sunday': 75.2
# }

# Write your code 👇 below:
def c_to_f(degree):
  return (degree * 9/5) + 32

weather_f = {day:c_to_f(degree) for (day, degree) in weather_c.items()}
print(weather_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
