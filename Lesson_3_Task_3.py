import random

nums = []
for i in range(15):
	nums.append(random.randint(1, 100))

mx = nums[0]
mn = nums[0]
for i in nums:
	if i > mx:
		mx = i
	if i < mn:
		mn = i

print(nums)
nums[nums.index(mx)] = mn
nums[nums.index(mn)] = mx
print(nums)
print(mx)
print(mn)
