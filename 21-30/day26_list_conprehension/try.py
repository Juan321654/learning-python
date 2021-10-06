# normal way
numbers = [1,2,3]
new_list = []
for n in numbers:
  add_1 = n + 1
  new_list.append(add_1)
# [2,3,4]


# Python way (Conprehension)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# [new_item for item in items if test]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)
# ['CAROLINE', 'ELEANOR', 'FREDDIE']

range_nums = range(1,5)
times_num = [n * 2 for n in range_nums]
print(times_num)
# [2, 4, 6, 8]