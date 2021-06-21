n = int(input("Введите n: "))
nums = []

for _ in range(n):
	nums.append((-0.5)**(n-1))
	n -= 1

print(sum(nums))