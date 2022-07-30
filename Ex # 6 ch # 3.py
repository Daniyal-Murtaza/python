# MODIFY NUMBER GUESSING GAME

# Here we will use RANDOM METHOD. Which will randomly select the number between given range.

import random
winning_number = random.randint(1,100)
Guess_number = int(input("Guess the winning number between 1 and 100:"))
Guess = 1
game_over = False               

while not game_over:
    if Guess_number == winning_number:
        print(f"Congratulations Bravo! You have won and you have guessed the winning number in {Guess} times")
        game_over = True

    else:
        if Guess_number < winning_number:
            print("Too low folk!")
            #Guess +=1
            #Guess_number = int(input("Guess again folk!:"))

        if Guess_number > winning_number:
            print("Too high folk!")
            #Guess +=1
            #Guess_number = int(input("Guess again folk!:"))

# we can write the above 2 commented lines in else block to avoid repeatition!
        Guess +=1
        Guess_number = int(input("Guess again folk!:"))

        


# This code is working but it is repeating itself in several places therefore now we will learn DRY coding principle which means 
# DON'T REPEAT YOURSELF!
# According this principle we will modify our code!

# like we are repeating the last 2 lines of nested if statements again so:
