from itertools import combinations

string_data = "homework"
unique_str = []
unique_hashes = []

for i in range(len(string_data)):
	for n in combinations(string_data, i):
		if hash(n) not in unique_hashes:
			unique_str.append(n)
			unique_hashes.append(hash(n))
print(unique_str)
print(f"Unique strings quantity: {len(unique_str)}")

