# for i in range(1, 11, 3):
#   print(i) # 1 4 7 10

# total = 0
# for number in range(1, 101):
#   total += number
# print(total) # 5050

even_total = 0
for number in range(1, 101):
  if number % 2 == 0:
    even_total += number
print(even_total)

another_even_total = 0
for number in range(1, 101, 2):
  another_even_total += number
print(another_even_total)