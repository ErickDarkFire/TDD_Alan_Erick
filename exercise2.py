"""
Exercise2
"""

def Add(nums):
    list_nums = nums.split(",")
    if nums == "":
        return 0
    if len(list_nums) == 1:
        return int(list_nums[0])
    else:
        acum = 0 
        for i in range(0,len(list_nums)):
            acum += int(list_nums[i])
        return acum