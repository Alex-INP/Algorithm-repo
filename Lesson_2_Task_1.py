while True:
	num_1 = int(input("Введите первое число: "))
	sign = input("Введите операцию: ")
	num_2 = int(input("Введите второе число: "))

	if sign == "+":
		print(num_1 + num_2)
	elif sign == "-":
		print(num_1 - num_2)
	elif sign == "*":
		print(num_1 * num_2)
	elif sign == "/":
		if num_2 == 0:
			print("Деление на ноль.")
		else:
			print(num_1 / num_2)
	elif sign == "0":
		break
	else:
		print("Не верная операция.")