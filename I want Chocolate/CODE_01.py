# title-I want Chocolate
# problem from CodeMania 2020(COM12020)
# cook your dish here
n,k=map(int,input().split())
p=list(map(int,input().split()))
total=0
sum=0
p.sort()
for i in p:
    sum+=i
    if sum<=k:
        total+=1
    else:
        break
print(total)
