import re
s=str(input())
v=r"[AEIOUaeiou]"
print(len(re.findall(v,s)))
