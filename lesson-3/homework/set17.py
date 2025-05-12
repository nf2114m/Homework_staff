x={1,2,3,4,5}
b1=[]
b={}
for i in x:
    if i%2!=0:
        b1.append(i)
b=set(b1)
print(b)
