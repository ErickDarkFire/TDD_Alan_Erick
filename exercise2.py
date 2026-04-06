"""
Exercise2
"""
def Add(nums):
    list_nums = nums.split(",")
    if len(list_nums) == 1 and list_nums[0] == "":
        return 0
    if len(list_nums) == 1:
        return int(list_nums[0])
    if len(list_nums) == 2:
        return int(list_nums[0]) + int(list_nums[1])