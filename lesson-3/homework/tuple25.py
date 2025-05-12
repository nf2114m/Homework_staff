a=(10, 3, 50, 21, 7, 15, 42, 1)
l=list(a)
s=[]
for i in l:
    if l.count(i)==1:
        s.append(i)
b=tuple(s)
print(b)
            
