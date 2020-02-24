# title-Lucky Number
# problem from CodeStart 2020(STRT2020)
# cook your dish here
t = int(input())
for i in range(t):
    n=input()
    n=[n[j:j+1] for j in range(0, len(n), 1)]
    for j in range(len(n)):
        n[j]=int(n[j])
    n.sort()
    for j in range(len(n)-1):
        if n[j+1]-n[j]==0 or n[j+1]-n[j]==1 or n[j+1]-n[j]==2:
            luck=True
        else:
            luck=False
            break
    if luck:
        print('YES')
    else:
        print('NO')
