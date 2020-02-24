# title-Reverse
# problem from IARCS OPC Judge Problems(IARCSJUD)
# cook your dish here
import string 
t=int(input())
rev=[]
for i  in range(t):
    s=input()
    t=''
    r=''
    for j in s:
        if not j in string.punctuation:
            t+=j 
    t=t.split()
    for j in t[::-1]:
        r+=j
        r+=' '
    rev.append(r)
for i in rev[::-1]:
    print(i)
