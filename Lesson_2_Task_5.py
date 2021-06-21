ent = 0
for i in range(32, 128):
	print(i, "-", chr(i), "| ", end="")
	ent += 1
	if ent % 10 == 0:
		print()


