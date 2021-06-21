import random

target = random.randint(0, 100)
attepts = 10

while True:
	print(f"У вас {attepts} попыток")
	if attepts == 0:
		print("Вы проиграли")
		break
		
	answer = int(input("Ваш вариант: "))
	if answer > target:
		print("Загаданное число меньше")
		attepts -= 1
	elif answer < target:
		print("Загаданное число больше")
		attepts -= 1
	else:
		print("Верно")
		break