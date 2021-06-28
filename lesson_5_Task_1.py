import collections as cln

firm = cln.namedtuple("Firm_info", ["firm_name", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])
firm_income = cln.namedtuple("Firm_with_middle_income", ["firm_name", "average"])

firm_number = int(input("Input firm quantity: "))
all_firms = []
for _ in range(firm_number):
	all_firms.append(firm(*input("Input data: ").split()))

all_firms_mid_income = []
for i in all_firms:
	all_firms_mid_income.append(firm_income(i.firm_name, (int(i.quarter_1) + int(i.quarter_2) + int(i.quarter_3) + int(i.quarter_4))/4))

all_mid_nums = []
for i in all_firms_mid_income:
	all_mid_nums.append(i.average)

total_average = sum(all_mid_nums)/len(all_mid_nums)
more_than_average = []
less_than_average = []
for i in all_firms_mid_income:
	if i.average > total_average:
		more_than_average.append(i)
	elif i.average < total_average:
		less_than_average.append(i)
print()
print("Average: ", total_average)
print("More than average firms:")
for i in more_than_average:
	print(f"Firm name: {i.firm_name} -- Firm average: {i.average}")
print("Less than average firms:")
for i in less_than_average:
	print(f"Firm name: {i.firm_name} -- Firm average: {i.average}")

