x={1,2,3,4,5}
y={1,6,7,4,8}
z1=x.intersection(y)
z2=y.intersection(x)
for i in z2:
    z1.add(i)
print(z1)
