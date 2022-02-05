#953. Verifying an Alien Dictionary
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

s = dict(zip(order,range(26)))

cursor = max( words,lambda v:len(v))
print(cursor)
