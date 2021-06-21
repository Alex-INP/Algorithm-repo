nums = input("Введите последовательность цифр: ")
trg_num = int(input("Введите искомую цифру: "))
cnt = 0

for i in list(nums):
	if int(i) == trg_num:
		cnt += 1

print(cnt)
