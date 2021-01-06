#1375. Bulb Switcher III
light = [4,1,2,3]
result=[]
c=0
l=len(light)
sum_list = (l*(l+1))//2
for i in range(len(light)):
    result.append(0)
print(result)
for i in light:
    result[i-1] = i
    flag = True
    for j in range(i,0,-1):
        print("Values",j)
        if j not in result:
            flag = False
            print("Problem",j)
            break
    if flag == True:
        if (sum(result[i:]==0) or (sum(result) ==sum_list)):
            print(result,j,i,result[i:],sum(result[i:]))
            c+=1
print(c)
        
    
5*6/2
