"""
Exercise2
"""
import re

def Add(nums):
    list_nums = re.split(r'[,\n]+',nums)
    if len(list_nums) == 1 and list_nums[0] == "":
        return 0
    elif len(list_nums) == 1:
        return int(list_nums[0])
    else:
        acum = 0
        for i in range(0,len(list_nums)):
            acum += int(list_nums[i])
        return acum