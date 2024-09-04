import random
jackpot=random.randint(1,100)

print('------ Enter Numbers Between 1 to 100 ------')
guess=int(input(("Chal guess kar: ")))
count=1
while guess!=jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess=int(input("Chal guess kar: "))
    count+=1
print("Congratulations!! Sahi Jawab")
print("You took",count,"attempts")