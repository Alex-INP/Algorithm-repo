import random

matrix = []
for i in range(10):
	matrix.append([])
for i in matrix:
	for _ in range(10):
		i.append(random.randint(1, 100))

for i in matrix:
	print(i)

min_elems = []
for n in range(10):
	column_nums = []
	for i in matrix:
		column_nums.append(i[n])
	min_elems.append(min(column_nums))

print("-"*40)
print(min_elems)
print(max(min_elems))