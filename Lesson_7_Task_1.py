import random
nums = [random.randint(-100, 100) for i in range(20)]
print(nums)

def bubble_sort(nums):
	for _ in range(len(nums)):
		for n in range(len(nums)-1):
			if nums[n] > nums[n+1]:
				nums[n], nums[n+1] = nums[n+1], nums[n]

bubble_sort(nums)
print(nums)