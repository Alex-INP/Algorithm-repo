from collections import defaultdict

string_data = ["defaultdict", "itertools", "abomination"]

for working_string in string_data:
	letter_cost = defaultdict(int)
	for i in working_string:
		letter_cost[i] += 1


	class Node:
		def __init__(self, name, cost, left=None, right=None):
			self.name = name
			self.cost = cost
			self.left = left
			self.right = right

		def __add__(self, other):
			if self.cost > other.cost:
				new_left = other
				new_right = self
			else:
				new_left = self
				new_right = other
			return Node(self.name + other.name, self.cost + other.cost, new_left, new_right)

		def __str__(self):
			return f"{self.name=}||{self.cost=}||{self.left=}||{self.right=}"


	all_nodes = [Node(key, val) for key, val in letter_cost.items()]


	def print_nodes(all_nodes):
		for i in all_nodes:
			print(f"{i.name} | {i.cost}")


	while len(all_nodes) != 1:
		all_nodes = sorted(all_nodes, key=lambda x: x.cost)
		all_nodes.append(all_nodes[0] + all_nodes[1])
		for i in range(2):
			all_nodes.remove(all_nodes[0])

	tree = all_nodes[0]

	letter_codes = {}
	for i in set(working_string):
		working_node = tree
		result_code = ""
		while len(list(working_node.name)) != 1:
			if i in working_node.left.name:
				working_node = working_node.left
				result_code += "0"
			elif i in working_node.right.name:
				working_node = working_node.right
				result_code += "1"
		letter_codes[i] = result_code

	print(f"Word: {working_string}")
	print(f"{letter_codes=}")
	final_code = ""
	for i in working_string:
		final_code += f"{letter_codes[i]} "

	print(f"Final code: {final_code[:-1]}\n")
