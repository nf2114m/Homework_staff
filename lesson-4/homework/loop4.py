import random

while True:
    ran=random.randint(1,100)
    for i in range(1,11):
        n=int(input(f"{i} try guess the number = "))
        if n==ran:
            print("You won")
            break
        elif n>ran:
            print("Too high!")
        else:
            print("Too low!")
        if i==11 and n!=ran:
            print("You lost")
    j=input("Want to play again?")
    if j in ["yes","YES","Y","y","ok"]:
        pass
    else:
        break
        
    
