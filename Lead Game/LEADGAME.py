# title-Lead Game
# problem from IARCS OPC Judge Problems(IARCSJUD)
# cook your dish here
r = int(input())
p1,p2=[],[]
leader=0
lead=0
for i in range(r):
    s1,s2=map(int,input().split())
    p1.append(s1)
    p2.append(s2)
for i in range(r-1):
    p1[i+1]=p1[i]+p1[i+1]
    p2[i+1]=p2[i]+p2[i+1]
for i in range(r):
    if p1[i]>p2[i]:
        l=p1[i]-p2[i]
        if l>lead:
            lead=l
            leader=1
    else:
        l=p2[i]-p1[i]
        if l>lead:
            lead=l
            leader=2
if leader:
    print(leader,lead)
