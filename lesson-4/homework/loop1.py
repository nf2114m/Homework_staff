list1=list(map(int,input(       ).split()))
list2=list(map(int,input().split()))

s=[]
for i in list1: 
    if i not in list2:
        s.append(i)
for i in list2:
    if i not in list1:
        s.append(i)
print(s)
