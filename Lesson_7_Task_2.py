import random

nums = [random.randint(0, 50) for i in range(21)]

def main_sort(nums):
    if len(nums) <= 1:
        return nums
    nums_1 = main_sort(nums[:len(nums) // 2])
    nums_2 = main_sort(nums[len(nums) // 2:])
    return process(nums_1, nums_2)

def process(nums_1, nums_2):
    sorted_list = []
    nums_1_ind, nums_2_ind = 0, 0
    for _ in range(len(nums_1) + len(nums_2)):
        if nums_1_ind < len(nums_1) and nums_2_ind < len(nums_2):
            if nums_1[nums_1_ind] <= nums_2[nums_2_ind]:
                sorted_list.append(nums_1[nums_1_ind])
                nums_1_ind += 1
            else:
                sorted_list.append(nums_2[nums_2_ind])
                nums_2_ind += 1
        elif nums_1_ind == len(nums_1):
            sorted_list.append(nums_2[nums_2_ind])
            nums_2_ind += 1
        elif nums_2_ind == len(nums_2):
            sorted_list.append(nums_1[nums_1_ind])
            nums_1_ind += 1
    return sorted_list

print(main_sort(nums))