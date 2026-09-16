from random import random

def get_color():
    value = random() * 100
    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    user_bilance = 1_000 
    print("Welcome to casino Roayal")
    while True:
        bet =  int(input(f"Select your bet ({user_bilance}eur):"))

        print("Select color:")
        print("\t\t0 - Red")   # 48.5%
        print("\t\t1 - White") # 48.5%
        print("\t\t2 - Green") # 3%
        print("\t\t3 - Leave game")
        selection = int(input("Select: "))

        if selection == 9: 
            return

        if selection == get_color():
            user_bilance = user_bilance + bet * 2
            print("You won!!")
        else:
            print(f"You lost {bet}eur")
            user_bilance = user_bilance - bet



if __name__ == "__main__":
    start_game()