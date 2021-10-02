# with open("weather_data.csv") as file:
#   data = file.readlines()
#   print(data)

# import csv

# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))

#   print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")

print(data[data.condition == "Rain"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
average_temp = sum(temp_list)/len(temp_list)
print(average_temp)  # 17.428571428571427

# the above lines for average temp can be reduce to a pandas function
print(data["temp"].mean())  # 17.428571428571427
print(data["temp"].max())  # 24

# Get data in row
print(data[data.day == "Monday"])  # 0  Monday    12     Sunny
print(data[data["day"] == "Monday"])  # 0  Monday    12     Sunny
print(data[data.temp == data.temp.max()])  # 6  Sunday    24     Sunny

monday = data[data.day == "Monday"]


def cel_to_fahr(cel):
    fahr = cel * (9.0/5.0) + 32.0
    return fahr


print(monday)  # 0  Monday    12     Sunny

print(cel_to_fahr(monday.temp))  # 53.6


# Create a dataframe from scratch

student_data_dict = {
  "students" : ["Amy", "James", "Juan"],
  "scores": [76, 56, 80]
}

student_data = pandas.DataFrame(student_data_dict)
print(student_data) 
# students  scores
# 0      Amy      76
# 1    James      56
# 2     Juan      80

student_data.to_csv("new_student_data.csv") # creates a csv on the file system