#1375. Bulb Switcher III
light = [2,1,3,5,4]
result=[]
c=0
l=len(light)
sum_list = (l*(l+1))//2
for i in range(len(light)):
    result.append(0)
for i in light:
    result[i-1] = i
    flag = True
    for j in range(i,0,-1):
        if j not in result:
            flag = False
            break
    if flag == True:
        print("len(result)",len(result))
        print("Check",result.count(0),(len(result)-i),result,i)
        if result.count(0)==(len(result)-i-1):
            c+=1
        '''
        for k in range(len(result)-1,-1,-1):
            print(
            if sum(result[k:-1]) == (((k+1)*(k+2))//2):
                c+=1
                break'''
        
        
print(result,c)
        
    
