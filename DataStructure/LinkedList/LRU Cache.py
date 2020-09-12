class LruCache(object):
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=[]
        self.Lru={}
        self.tm=0
        
    def get(self,key):
        #Get the Data from Cache
        if key in self.cache:#If Key Exist in Cache
            self.lru[key]=self.tm
            self.tm+=1
            print("Cache = ")
            return 1
        else:
            return -1
    def set(self,key):
        if len(self.cache)>self.capacity:
            if key not in self.Lru: 
                #Find Least Entry
                old_Key=min(self.Lru.keys(),key=lambda k:self.Lru[k])#Vary Important Logic
                #print("Old Value ======",old_Key)
                #Just Delete Old Value
                for i in range(len(self.cache)):
                    if self.cache[i]==old_Key:
                        self.cache.pop(i)
                        print("Duplicate",self.cache)
                        break
                    
                self.Lru.pop(old_Key)

            
                self.Lru[key]=self.tm
                self.cache.append(key)
                self.tm+=1
            else:
                self.Lru[key]=self.tm
                self.tm+=1
                
        else:

            if key in self.Lru:
                self.Lru[key]=self.tm
                self.tm=self.tm+1
            else:
                self.cache.append(key)
                self.Lru[key]=self.tm
                self.tm+=1
        #print("LRU: {}".format(self.Lru))
        print("Cache : {}".format(self.cache))

if __name__=="__main__":
    l1=LruCache(capacity=3)
    l1.set(1)
    l1.set(2)
    l1.set(3)
    l1.set(3)
    l1.set(1)
    l1.set(5)
    l1.set(2)
    l1.set(8)
