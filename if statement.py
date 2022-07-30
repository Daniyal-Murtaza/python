# syntax
# if condition:
#     #code #if the condition is true then the condition will execute
#     #code

# Assume you are making a game that only kids above 14 can play then you have to use IF SYTEMENT in your code

age = input("Enter your age:")       # but python always take the input in the form of string data type therefore we will first change it onto integer data type!
age = int(age)                       # we can also do it in the above line by age = int(input("Enter your age:"))
if age > 14:
    print("You are eligible to play this game! XD")    # this is called IF BLOCK! indentation is necessary in the block of IF STATEMENT
                
