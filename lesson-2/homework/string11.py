import re
s=str(input())
n=r"[1234567890]"
print("not contains" if len(re.findall(n,s))==0 else "contains")
