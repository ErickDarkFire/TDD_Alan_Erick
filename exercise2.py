"""
Exercise2
"""

def Add(nums):
    if nums == "":
        return 0
    
    sep = [',','\n']
    size = len(nums)
    if size > 2 and nums.startswith("//"):
            header, nums = nums.split("\n", 1)
            size = len(nums)
            sep = [header[2:]]

    if any(nums.endswith(d) for d in sep):
        raise ValueError("Invalido")
    
    #remplazamos todos los separadores por 1 solo
    s = sep[0]
    for i in range(1,len(sep)):
        nums = nums.replace(sep[i],s)
    list_nums = nums.split(s)  

    new_nums = []
    for x in list_nums:
        if x.strip():
            new_nums.append(x)
    list_nums = new_nums     
    
    acum = 0 
    negative_numbers = []
    for i in range(0,len(list_nums)):
        try:
            n = int(list_nums[i])
            if n < 0:
                negative_numbers.append(str(n))
            else:
                acum += n
        except:
            for x in list_nums[i]:
                if x.isdigit() == False:
                    raise ValueError(f"'{''.join(sep)}' expected but '{x}' found at position {nums.find(x)}")
    
    if len(negative_numbers) > 0:
        raise ValueError(f"Negative number(s) not allowed: {','.join(negative_numbers)}")
    else:
        return acum