# title-Not All Flavours
# problem from  February Lunchtime 2020 Division 2
# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    c=input().split()
    def sub(list1,k):
        sublist=[[]]
        for m in range(len(list1) + 1):
            for n in range(m + 1, len(list1) + 1):
                sub = list1[m:n]
                sublist.append(sub)
        max=0
        ans=[]
        for m in sublist:
            if len(set(m))<k and len(m)>max:
               ans=m
               max=len(m)
        return len(ans)
    print(sub(c,k))