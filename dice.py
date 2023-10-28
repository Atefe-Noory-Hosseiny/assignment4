import random

while True:
    a=input("enter(roll the dice,exit):")

    
    if a=="roll the dice":
        dice=random.randint(1,6)
        print(dice)
        if dice == 6:
            dice=random.randint(1,6)
            print("walk 6 steps and roll again")
            
        else:
            print("walk",dice,"steps")
            break

    if a=="exit":
        break
   