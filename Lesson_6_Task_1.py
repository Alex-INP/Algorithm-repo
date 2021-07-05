# Алгоритм находит два наименьших числа из списка.

# Разрядность системы: 64
# Версия python: 3.8

import random

nums = []  # Для 50 чисел: (24*50)+(40+8*50)=1200+440=1640
for i in range(50):
	nums.append(random.randint(1, 100))

# Вариант 1.
def var_1(nums):
	mn = nums[0]  # (24*1)=24
	mn_2 = nums[0]  # --//--
	for i in nums:
		if i < mn:
			mn = i  # --//--

	mn_indx = nums.index(mn)  # --//--
	for i in nums:
		if i < mn_2 and nums.index(i) != mn_indx:
			mn_2 = i  # --//--

	print(nums)
	print(mn)
	print(mn_2)


var_1(nums)

# Определение места букв в алфавите и количество букв междй ними.
import string

letter_1 = input()  # (37+1)=38
letter_2 = input()  # --//--

letter_1_place = string.ascii_lowercase.index(letter_1) + 1  # (24*1)=24
letter_2_place = string.ascii_lowercase.index(letter_2) + 1  # --//--

print(letter_1_place)
print(letter_2_place)
print(letter_2_place - letter_1_place - 1)

# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

lis_1 = input("Первая строка: ").split() # При условии 5 объектов в списке: (24*5)+(40+8*5)=120+80=200
lis_2 = input("Вторая строка: ").split() # --//--
lis_3 = input("Третья строка: ").split() # --//--
lis_4 = input("Четвертая строка: ").split() # --//--

for lis_s in (lis_1, lis_2, lis_3, lis_4):
	for ind, val in enumerate(lis_s):
		lis_s[ind] = int(val)

lis_1.append(sum(lis_1))
lis_2.append(sum(lis_2))
lis_3.append(sum(lis_3))
lis_4.append(sum(lis_4))

print(f'{lis_1}\n{lis_2}\n{lis_3}\n{lis_4}')
