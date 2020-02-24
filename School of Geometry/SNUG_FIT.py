# title-School of Geometry
# problem from February Challenge 2020 Division 2
# cook your dish here
t=int(input())
for i in range(0,t):
    n=int(input())
    A=map(int,input().split())
    B=map(int,input().split())
    a=sorted(A)
    b=sorted(B)
    sum=0
    for i in range(0,n):
        if(a[i]<b[i]):
            sum+=a[i]
        else:
            sum+=b[i]
    print(sum)
