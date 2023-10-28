import random

pc_number =random.randint(0,20)
guess=0
while True:
    user_number=int(input("enter a number:"))
    guess+=1

    if user_number == pc_number:
        print("great")
        break

    if user_number < pc_number:
        print("enter a bigger number")

    if user_number > pc_number:
        print("enter a smaller number")

print("you've gussed:",guess,"times")