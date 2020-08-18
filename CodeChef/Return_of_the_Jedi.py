'''
On the ice planet Hoth, Chef has run into his arch-nemesis,
DarthForces. Darth has a peculiar fighting style ― he does not
attack, but simply defends and lets his opponent tire himself
out.

Chef has a lightsaber which has an attack power denoted by P. He keeps hitting Darth with the lightsaber. Every time he hits, Darth's health decreases by the current attack power of the lightsaber (by P points), and afterwards, P decreases to ⌊P2⌋.
'''
n=int(input())
for i in range(n):
    H,P=map(int,input().split())
    while(True):
        H=H-P
        if P<=0 and H!=0:
            print(0)
            break
        elif P!=0 and H<=0:
            print(1)
            break
        P=P//2
        

