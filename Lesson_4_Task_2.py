import timeit

target_num = int(input("Укажите порядковый номер простого числа: "))


def eratos(target_num):
	n = target_num * 15
	a = [0] * n
	for i in range(n):
		a[i] = i

	a[1] = 0

	m = 2
	while m < n:
		if a[m] != 0:
			j = m * 2
			while j < n:
				a[j] = 0
				j += m
		m += 1

	for _ in range(a.count(0)):
		a.remove(0)

	print(a)
	print("Искомое число: ", a[target_num - 1])


def not_eratos(target_num):
	num = 2
	counter = 0
	all_nums = []
	while counter != target_num:
		flag = True
		for i in range(1, num):
			if num % i == 0 and i != 1 and i != num:
				flag = False
				break
		if flag:
			all_nums.append(num)
			counter += 1

		num += 1

	print(all_nums)
	print("Искомое число:", all_nums[-1])


print(timeit.timeit(f'{eratos(target_num)}'))
print(timeit.timeit(f'{not_eratos(target_num)}'))

# Разницы в скорости выполнения практически нет:
# eratos(target_num) за 0.0071246999999985405,
# not_eratos(target_num) за 0.0074380000000005.
# Сложность выполнения алгоритмов O(n**2)
