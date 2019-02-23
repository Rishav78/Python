import random
chance=1
number = random.randint(1,100)
while True:
    num = int(input("Enter A Number "))
    if num==number or chance==5 :
        if chance==5:
            print("You have loose all your chance")
        else:
            print("You Win")
        break
    else:
        if num<12 :
            print("Too low")
        else:
            print("Too high")
    chance = chance + 1