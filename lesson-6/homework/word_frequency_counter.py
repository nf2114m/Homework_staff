with open("sample.txt", "r") as file:
    text = file.read()

rm = ',.!?(){}[]'
for i in rm:
    text = text.replace(i, '')

text = text.lower()

words = text.split()

words2=[]
for i in words:
    if i=="a" or i=="an" or i=="the":
        pass
    else:
        words2.append(i)
    
words3=set(words2)

wd=[]
ct=[]

for i in words3:
    wd.append(i)
    ct.append(words2.count(i))
print("Total words:",len(words2))
print("Top 5 most common words")
for i in range(5):
    ind=ct.index(max(ct))
    print(f"{wd[ind]}-{ct[ind]}")
    wd.pop(ind)
    ct.pop(ind)
    
