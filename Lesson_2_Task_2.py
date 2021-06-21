num = input("Введите число: ")
ch, ne_ch = [], []
for i in list(num):
	if int(i) % 2 == 0:
		ch.append(i)
	else:
		ne_ch.append(i)

print(f"Четные: {ch}")
print(f"Не четные: {ne_ch}")
