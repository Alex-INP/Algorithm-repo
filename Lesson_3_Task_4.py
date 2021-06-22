import random

nums = []
for i in range(25):
	nums.append(random.randint(1, 15))

print(nums)
trg_num = None
cnt = 0
for i in nums:
	processing_num = i
	processing_cnt = 0
	for n in nums:
		if n == i:
			processing_cnt += 1
	if processing_cnt >= cnt:
		cnt = processing_cnt
		trg_num = processing_num

print(trg_num, "|", cnt)
