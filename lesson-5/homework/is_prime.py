def is_prime(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+1
    if s==1:
        print(True)
    else:
        print(False)
n=int(input("Enter:  "))
is_prime(n)
