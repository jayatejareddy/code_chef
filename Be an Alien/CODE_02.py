# title-Be an Alien
# problem from CodeMania 2020(COM12020)
# cook your dish here
lan=[]
alien=[]
for i in range(6):
    r=input()
    lan.append(r)
for i in lan:
    alien.append(i[::-1])
alien=alien[::-1]
for i in alien:
    print(i)
