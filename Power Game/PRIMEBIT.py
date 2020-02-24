# title-Power Game
# problem from CodeStart 2020(STRT2020)
# cook your dish here
t= int(input())
for i in range(t):
    p=int(input())
    sum=0
    p=list(bin(p).replace('0b',''))[::-1]
    res=[j for j,x in enumerate(p) if x == '1']
    for j in res:
        sum+=j
    print(sum)
