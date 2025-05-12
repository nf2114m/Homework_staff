import random
n=5
m=10
s=[]
for i in range(n):
    s.append(random.randint(0,m))
s=set(s)
print(s)
