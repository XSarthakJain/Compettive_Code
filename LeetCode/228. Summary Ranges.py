#228. Summary Ranges
result = []
        if len(nums) == 0:
            return 
        beg = nums[0]
        temp = nums[0]
        for index,item in enumerate(nums):
            if ((item == temp+1) and (index!=0)):
                temp = item
            elif index!=0:
                result.append(f"{beg}->{temp}"if beg!=temp else str(beg))
                beg = item
                temp = item
        result.append(f"{beg}->{temp}"if beg!=item else str(beg))
        return result
