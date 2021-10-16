# try:
#   file = open("a_file.txt")
#   a_dictionary = {"key": "value"}
#   # print(a_dictionary["fhdjskfhjdsk"]) # this will cause a key error
#   print(a_dictionary["key"])
# except FileNotFoundError:
#   file = open("a_file.txt", "w") #w will create a file if there is not one already
#   file.write("Something")
# except KeyError as error_message:
#   print(f"The key {error_message} does not exist.")
# else:
#   content = file.read()
#   print(content)
# finally:
#   file.close()
#   print("File was closed.")

# try:
#   file = open("a_file.txt")
#   a_dictionary = {"key": "value"}
#   # print(a_dictionary["fhdjskfhjdsk"]) # this will cause a key error
#   print(a_dictionary["key"])
# except FileNotFoundError:
#   file = open("a_file.txt", "w") #w will create a file if there is not one already
#   file.write("Something")
# except KeyError as error_message:
#   print(f"The key {error_message} does not exist.")
# else:
#   content = file.read()
#   print(content)
# finally:
#   raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)