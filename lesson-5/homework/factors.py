def factors(number):
    factors = list(filter(lambda factor: number%factor==0,range(1, number+1)))
    for i in factors:
        print(f"{i} is a factor of {number}")
        

factors(int(input("Enter a positive integer: ")))

