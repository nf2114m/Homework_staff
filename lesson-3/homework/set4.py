a={0, 4, 7, 8, 12, 14, 15}
b={0, 4, 7}
a1=list(a)
b1=list(b)
s=False
for i in range(len(a1)):
    if b1==a1[i:len(b1)+i]:
        s=True
print(s)
