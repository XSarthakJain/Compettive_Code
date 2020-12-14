#Print all possible palindromic string formed using any pair of given strings
'''
Given an array of strings arr[] containing N words, the task is to print all possible palindromic string by combining any two strings from the given array.

Examples:

Input: arr[] = [“geekf”, “geeks”, “or”, “keeg”, “abc”, “ba”]
Output: [“geekfkeeg”, “geekskeeg”, “abcba”]  
Explanation:
Below pairs forms the palindromic string on combining:
1. “geekf” + “keeg” = “geekfkeeg”
2. “geeks” + “keeg” = “geekskeeg”
3. “abc” + “ba” = “abcba”

Input: arr[] = [“dcb”, “yz”, “xy”, “efg”, “yx”] 
Output: [“xyyx”, “yxxy”]
Explanation:
1. “xy” + “yz” = “xyyz”
2. “yx” + “xy” = “yxxy”
'''
#https://www.geeksforgeeks.org/print-all-possible-palindromic-string-formed-using-any-pair-of-given-strings/?ref=rp
#geekf geeks or keeg abc ba
output=[]
def palindromic(s,current):
    if current==len(s):
        return
    else:
        
        for i in range(len(s)):
            if i==current:
                continue
            if (s[i]+s[current])==((s[i]+s[current])[::-1]):
                if (s[i]+s[current]) not in output:
                    output.append(s[i]+s[current])
            elif (s[current]+s[i])==((s[current]+s[i])[::-1]):
                if (s[current]+s[i]) not in output:
                    output.append(s[current]+s[i])
        palindromic(s,current+1)
        



n=list(map(str,input().split()))
print(palindromic(n,0))
print(output)
