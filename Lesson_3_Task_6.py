import random

nums = []
for i in range(10):
	nums.append(random.randint(1, 10))

mx = nums[0]
mn = nums[0]
for i in nums:
	if i > mx:
		mx = i
	if i < mn:
		mn = i

print(nums)
print(mx)
print(mn)
fin_sum = sum(nums[nums.index(mn) + 1: nums.index(mx)])
if fin_sum == 0:
	fin_sum = sum(nums[nums.index(mx) + 1:  nums.index(mn)])

print(fin_sum)
