import random

nums = []
for i in range(50):
	nums.append(random.randint(1, 100))

min = nums[0]

for i in nums:
	if i < min:
		min = i

print(nums)
print(min)
