#599. Minimum Index Sum of Two Lists
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
resultScore = 1000000
        resultValue = []
        for index,i in enumerate(list1):
            try:
                if list2.index(i)>=0 and resultScore>=(index+list2.index(i)):
                    if resultScore>(index+list2.index(i)) and resultScore!=1000000:
                        del resultValue[-1]
                    resultScore = index+list2.index(i)
                    resultValue.append(i)            
            except:
                pass
return resultValue
