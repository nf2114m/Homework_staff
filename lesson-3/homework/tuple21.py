a=(10, 3, 50, 21, 7, 15, 42, 1)
n=3
l=[]
for i in a:
    for j in range(n):
        l.append(i)
b=tuple(l)
print(b)
