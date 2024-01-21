num = 58
result = ''
roman = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
pointer = 0
while(num!=0):
    print(pointer,num,result,list(roman.values())[pointer])
    if num>=list(roman.values())[pointer]:
        result+= str(list(roman.keys())[pointer])*(num//list(roman.values())[pointer])
        num = num%list(roman.values())[pointer]
    pointer+=1
print(result)
