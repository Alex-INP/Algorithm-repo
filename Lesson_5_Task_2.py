letters_nums = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
nums_letters = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
# num_1 = "a2"
# num_2 = "c4F"
num_1 = input("Input number 1: ")
num_2 = input("Input number 2: ")

num_1_l = []
num_2_l = []
def convert_to_nums(num, num_l):
	for i in list(num):
		if i.isdigit():
			num_l.append(int(i))
		else:
			num_l.append(letters_nums[i.upper()])

def convert_to_10(num_l):
	final_num = 0
	for ind, val in enumerate(list(reversed(num_l))):
		final_num += val*16**ind
	return final_num

def convert_to_nums_l(num):
	final_num_l = []
	while True:
		ost = num % 16
		num = num // 16
		final_num_l.append(ost)
		if num <= 15:
			final_num_l.append(num)
			break
	return final_num_l

def convert_to_16(num):
	target = ""
	for i in list(reversed(convert_to_nums_l(num))):
		if i > 9:
			target = target + nums_letters[str(i)]
		else:
			target = target + str(i)
	return target

convert_to_nums(num_1, num_1_l)
convert_to_nums(num_2, num_2_l)

add_calc_result = convert_to_10(num_1_l) + convert_to_10(num_2_l)
mult_calc_result = convert_to_10(num_1_l) * convert_to_10(num_2_l)

print(f'{num_1} + {num_2} = {convert_to_16(add_calc_result)}')
print(f'{num_1} * {num_2} = {convert_to_16(mult_calc_result)}')

