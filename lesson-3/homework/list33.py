l=[1, 2, 3, 2, 4, 5, 3]
n=3
ln=l.count(n)
for i in range(len(l)):
    if l[i]==n:
        print(i)
