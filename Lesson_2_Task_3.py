num = input("Введите число: ")
mun = ""
ind = -1

for i in num:
	mun += num[ind]
	ind -= 1

print("Результат:", mun)