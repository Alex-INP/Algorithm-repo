nums = input("Введите несколько натуральных чисел через запятую: ").split(",")
processed_nums = {}

def sum_f(n):
	fin_num = 0
	for i in list(n):
		fin_num += int(i)
	return fin_num

for i in nums:
	processed_nums[sum_f(i)] = i

max_key = max(processed_nums.keys())
print(processed_nums[max_key], "-", max_key)
