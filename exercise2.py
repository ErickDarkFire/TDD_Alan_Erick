"""
Exercise2
"""

def Add(nums):
    if nums == "":
        return 0
    error_msg = []
    error_msg2 = [] #Para agregar al final los separadores que no coincidan

    sep = [',','\n']
    size = len(nums)
    if size > 2 and nums.startswith("//"):
            header, nums = nums.split("\n", 1)
            size = len(nums)
            sep = [header[2:]]

    if any(nums.endswith(d) for d in sep):
        error_msg.append("Invalid")
        #raise ValueError("Invalid")
    
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
            if n < 1000 and n > 0:
                acum += n
            if n < 0:
                negative_numbers.append(str(n))
        except:
            for l in range(len(list_nums[i])):
                x = list_nums[i][l]
                #"2,-3"
                if x.isdigit() == False and x != "-":
                    error_msg2.append(f"'{''.join(sep)}' expected but '{x}' found at position {nums.find(x)}")
                if x == "-":
                    l+=1
                    x = list_nums[i][l]
                    numero_negativo = "-"
                    while l < len(list_nums[i]) and x.isdigit():
                        numero_negativo += x
                        l += 1
                        if l < len(list_nums[i]):
                            x = list_nums[i][l]
                    try:
                        int(numero_negativo)
                        negative_numbers.append(numero_negativo)
                    except:
                        pass


    if len(negative_numbers) > 0:
        error_msg.append(f"Negative number(s) not allowed: {','.join(negative_numbers)}")
    
    if len(error_msg) > 0 or len(error_msg2) > 0:
        error_msg.extend(error_msg2)
        raise ValueError("\n".join(error_msg))
    else:
        return acum