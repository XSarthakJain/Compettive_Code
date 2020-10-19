#Find the Duplicate Number
num=list(map(int,input().split()))
for i in range(len(num)):
            if num[i]!=(i+1):
                if num[num[i]-1]!=num[i]:
                    print(num[i],num[num[i]-1])
                    num[i],num[num[i]]=num[num[i]],num[i]
                else:
                    print(num[i])
print(num)
