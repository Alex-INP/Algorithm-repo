import copy
import random

m = 6
nums = [random.randint(0, 100) for i in range(2 * m + 1)]
print(nums)

mediana = nums[0]
more = 0
less = 0
for i in nums:
	for f in nums:
		if i > f:
			more += 1
		elif i < f:
			less += 1
		else:
			more += 1
			less += 1
	if more == less:
		mediana = i
		break
	more, less = 0, 0

print(f"{mediana=}")

# f = copy.copy(nums)
# mid = len(f) // 2
# print(sorted(f))
# print(sorted(f)[mid])
