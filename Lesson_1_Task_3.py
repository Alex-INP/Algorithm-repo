x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

k = (y_2 - y_1) / (x_2 - x_1)
b = y_1 - k * x_1

print(f"{k = } {b = }")