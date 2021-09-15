def greet(name, location):
  print(f"hello {name}")
  print(f"hello from {location}")

greet("Juan", "New york")

def positional_greet(name, location):
  print(f"hello {name}")
  print(f"hello from {location}")

positional_greet(location="New York", name="Juan") # this does not work in Javascript