p=input()
if len(p)<7:
    print("Password is too short.")
elif any(i.isupper() for i in p):
    print("Password is strong")
else:
    print("Password must contain an uppercase letter.")
