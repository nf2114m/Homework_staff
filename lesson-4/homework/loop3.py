banned="euioa"
s=input()
out=""
n=1
for i in range(len(s)):
    if i>n and s[i] not in banned:
        out=out+s[i]+"_"
        banned=banned+s[i]
        n=i+2
        
    else:
        out=out+s[i]
if out[-1]=="_":
    out=out[0:-1]
print(out)

