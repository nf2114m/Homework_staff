l=[1, 2, 3, 2, 4, 5, 3]
l2=[]
for i in range(len(l)):
    x=l.count(l[i])
    if x==1:
        l2.append(l[i])
print(l2)
