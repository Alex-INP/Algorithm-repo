lis_1 = input("Первая строка: ").split()
lis_2 = input("Вторая строка: ").split()
lis_3 = input("Третья строка: ").split()
lis_4 = input("Четвертая строка: ").split()

for lis_s in (lis_1, lis_2, lis_3, lis_4):
	for ind, val in enumerate(lis_s):
		lis_s[ind] = int(val)

lis_1.append(sum(lis_1))
lis_2.append(sum(lis_2))
lis_3.append(sum(lis_3))
lis_4.append(sum(lis_4))

print(f'{lis_1}\n{lis_2}\n{lis_3}\n{lis_4}')