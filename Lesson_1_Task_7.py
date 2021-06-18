len_a = int(input())
len_b = int(input())
len_c = int(input())

if len_a + len_b > len_c and len_a + len_c > len_b and len_b + len_c > len_a:
	print("Существует")
	if len_a == len_b and len_b == len_c:
		print("Равносторонний")
	elif len_a == len_b or len_b == len_c or len_c == len_a:
		print("Равнобедренный")
	else:
		print("Разносторонний")
else:
	print("Не существует")
