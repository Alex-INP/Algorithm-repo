num = int(input("Введите натуральное число: "))

def sum_f(n):
	if n == 0:
		return n
	return n + sum_f(n - 1)

print(sum_f(num), "=", num*(num+1)/2)
