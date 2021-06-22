import random

nums = []
for i in range(50):
	nums.append(random.randint(1, 100))

print(nums)


mn = nums[0]
mn_2 = nums[0]
for i in nums:
	if i < mn:
		mn = i

mn_indx = nums.index(mn)

for i in nums:
	if i < mn_2 and nums.index(i) != mn_indx:
		mn_2 = i

print(mn)
print(mn_2)