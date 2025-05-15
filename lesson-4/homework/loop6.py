for i in range(1,101):
    s=0
    for j in range(2,i):
        if i%j==0:
            s=s+1
    if s==0:
        print(i)
    else:
        s=0
