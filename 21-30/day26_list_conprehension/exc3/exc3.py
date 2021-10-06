with open("file1.txt") as file:
  content = file.readlines()
with open("file2.txt") as file_2:
  content_2 = file_2.readlines()
  
result = [int(n) for n in content if n in content_2]
# Write your code above 👆

print(result)

