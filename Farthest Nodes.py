#Farthest Nodes

'''
Have the function FarthestNodes(strArr) read strArr which will be an array of hyphenated letters representing paths between those two nodes. For example: ["a-b","b-c","b-d"] means that there is a path from node a to b (and b to a), b to c, and b to d. Your program should determine the longest path that exists in the graph and return the length of that path. So for the example above, your program should return 2 because of the paths a-b-c and d-b-c. The path a-b-c also means that there is a path c-b-a. No cycles will exist in the graph and every node will be connected to some other node in the graph.
Examples
Input: ["b-e","b-c","c-d","a-b","e-f"]
Output: 4
Input: ["b-a","c-e","b-c","d-c"]
Output: 3
'''


path=dict()

def fun(b):
    if b not in path:
        return 0
    else:
       return 1+fun(path[b])
    
def FarthestNodes(strArr):

  # code goes here
  
  l=0
  for i in strArr:
    if i[0] in path:
      
      path[i[0]].append(i[2])
    else:
      path[i[0]]=[i[2]]
    
    for i in path:
        for j in range(len(i)):
            print((path[i][j]),path)
            #l=max(l,fun(i[j]))
            print(l)
            
  return l

# keep this function call here 
print(FarthestNodes(["b-e","b-c","c-d","a-b","e-f"]))
