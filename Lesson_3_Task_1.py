nums = list(range(2, 100))

for n in (2,3,4,5,6,7,8,9):
	num_count = 0
	for i in nums:
		if i % n == 0:
			num_count += 1
	print(n, "|", num_count)