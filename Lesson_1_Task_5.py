import string
letter_1 = input()
letter_2 = input()

letter_1_place = string.ascii_lowercase.index(letter_1) + 1
letter_2_place = string.ascii_lowercase.index(letter_2) + 1


print(letter_1_place)
print(letter_2_place)
print(letter_2_place - letter_1_place - 1)