#You have been given longitude and latitude of locations from where the channels are going to be broadcasted.
#You also get the height of tower from which these channels are broadcasted. Moreover, you have been given
#the location of your friend Jason. You have to calculate how many connections he can make to the towers.
#Take Radius of earth= 6371 KM.

from math import sin, cos, sqrt, asin,radians
n = int(input())


count=0
lati = list(map(float,input().split()))
longit = list(map(float,input().split()))
towerHeight = list(map(float,input().split()))
person_Lati,person_Long=map(float,input().split())
    
    
    
for j in range(len(lati)):
    lat1 = radians(lati[j])
    lon1 = radians(longit[j])
    lat2 = radians(person_Lati)
    lon2 = radians(person_Long)
        
    dlon = lon2 - lon1
    dlat = lat2 - lat1
        
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 6371*2 * asin(sqrt(a))
        
    tower = (2*6371*towerHeight[j])**0.5
    if tower > c or tower == c:
        count +=1
        tower = 0
        

    
print(count)
