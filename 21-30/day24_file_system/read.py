# file = open("my_file.txt")
# contents = file.read()

# print(contents)

# file.close()
# if you use open, you have to close the file manually like in line 6, instead use the following:


# Read
with open("../../my_file.txt") as file:
  contents = file.read()

# Write    mode = w = writable
with open("../../my_file.txt", mode="w") as file:
  file.write("New text.")

# Append text
with open("../../my_file.txt", mode="a") as file:
  file.write("\nNew text with append.")
  print(contents) 
  