import random
winning_num=random.randint(1,100)
guess=1
num=int(input("guess a number between 1 and 100 : "))
game_over=False
while not game_over:
    if num == winning_num:
        print(f"you win,and you guessed this number in {guess} times")
        game_over=True
    else:
        if num<winning_num:
            print("too low")
        else:
            print("too high")
        guess += 1
        num=int(input("guess again: "))