# Алгоритм находит два наименьших числа из списка.
import timeit
import random

nums = []
for i in range(50):
	nums.append(random.randint(1, 100))

# Вариант 1.
def var_1(nums):
	mn = nums[0]
	mn_2 = nums[0]
	for i in nums:
		if i < mn:
			mn = i

	mn_indx = nums.index(mn)
	for i in nums:
		if i < mn_2 and nums.index(i) != mn_indx:
			mn_2 = i

	print(nums)
	print(mn)
	print(mn_2)

# Вариант 2
def var_2(nums):
	mn = nums[0]
	print(nums)
	for i in nums:
		if i < mn:
			mn = i

	nums.remove(mn)
	mn_2 = nums[0]
	for i in nums:
		if i < mn_2:
			mn_2 = i

	print(mn)
	print(mn_2)

print(timeit.timeit(f"{var_1(nums)}"))
print(timeit.timeit(f"{var_2(nums)}"))
# Время исполнения var_1 = 0.0088535, var_2 = 0.013398199999999999.
# Сложность обоих алгоритмов O(n).