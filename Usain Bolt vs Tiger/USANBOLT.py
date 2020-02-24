# title-Usain Bolt vs Tiger
# problem from ICPC Asia-Amritapuri Onsite Replay Contest 2019
# cook your dish here
import math
t=int(input())
for _ in range(t):
    s,d,a,v=map(int,input().split())
    t1=math.sqrt(2*(s+d)/a)
    t2=s/v
    if t2<t1:
        print('Bolt')
    else:
        print('Tiger')
