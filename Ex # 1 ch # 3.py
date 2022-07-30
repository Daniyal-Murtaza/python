# EXERCISE : NUMBER GUESSING GAME!

# Make a variable winning_number and assign any number to it
# Ask the user to guess the number
# if user guessed correctly then print Congratulations! You Win!!!

winning_number = 5
Guess_number = int(input("Guess the winning number! Hint: It is between 1-10:"))
if winning_number == Guess_number:
    print("Congratulations! You Win!!!")
else:
    if Guess_number < winning_number:
        print("too low")
    if Guess_number > winning_number:               
        print("too high")

    # we can also write last 2 lines like these with the same indentations!
    #else:
        #print("too high")