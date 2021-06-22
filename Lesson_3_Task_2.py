import random

nums = []
inds = []
for i in range(15):
	nums.append(random.randint(1, 100))
for i in nums:
	if i % 2 == 0:
		inds.append(nums.index(i))

print(nums)
print(inds)
