# title-List of Books
# problem from IARCS OPC Judge Problems(IARCSJUD)
# cook your dish here
m=int(input())
b=list(map(int,input().split()))
t=int(input())
for i in range(t):
    e=int(input())
    print(b[e-1])
    b.pop(e-1)
    