import random

c=0
p=0

while True:
    a=random.choice(["rock","paper","scissors"])
    b=input()
    if a=="rock" and b=="paper":
        p=p+1
        print(a)
        print("comp:",c," you:",p)
    if a=="paper" and b=="rock":
        c=c+1
        print(a)
        print("comp:",c," you:",p)
    if a=="rock" and b=="scissors":
        c=c+1
        print(a)
        print("comp:",c," you:",p)
    if a=="scissors" and b=="rock":
        p=p+1
        print(a)
        print("comp:",c," you:",p)
    if a=="scissors" and b=="paper":
        c=c+1
        print(a)
        print("comp:",c," you:",p)
    if a=="paper" and b=="scissors":
        scoreplay=scoreplay+1
        print(a)
        print("comp:",c," you:",p)
    if a==b:
        print(a)
        print("comp:",c," you:",p)
    if c==5:
        print("you lost")
        break
    if p==5:
        print("you won")
        break

        
