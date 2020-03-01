# title-At the Gates
# problem from  February Lunchtime 2020 Division 2
# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    coins=input().split()
    c=0
    for j in range(k):
        temp=[]
        if coins[len(coins)-1]=='H':
            coins.pop(len(coins)-1)
            for x in coins:
                if x=='H':
                    temp.append('T')
                else:
                    temp.append('H')
            coins=temp
        else:
            coins.pop(len(coins)-1)
    for j in coins:
        if j=='H':
            c+=1
    print(c)