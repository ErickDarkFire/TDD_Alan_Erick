"""
Exercise2
"""
import re

def Add(nums):
    if nums == "":
        return 0
    
    sep = [',','\n']
    size = len(nums)
    if nums[size-1] in sep:
        raise ValueError("Invalido")
    
    list_nums = re.split(r'[,\n]+',nums)
    if size == 1:
        return int(list_nums[0])
    else:
        acum = 0 
        for i in range(0,len(list_nums)):
            acum += int(list_nums[i])
        return acum