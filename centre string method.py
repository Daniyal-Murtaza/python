# center method (IT IS A METHOD SO YOU KNOW VERY WELL WHAT THE SYNTAX WILL BE)
# it is used to specify the strig in the middle of special characters like asterisk.

name = "Daniyal"
print(name.center(12,"*"))
#                here you will give the number of alphabets in the name + asterisk you want to add on both the sides!t
# if the asterisk to be added is coming more then it will be on the right hand side

print(name.center(11,"*"))
print(name.center(8,"*"))

# No w we are writing the program to let the user input their text in which 4 asterisk should be added on both sides!
name = input("Enter your name:")
print(name.center(len(name) + 8,"*"))

# REMEBER LEN IS A FUNCTION THEREFORE IT'S SYNTAX IS DIFFERENT THEN METHOD LIKE LOWER, UPPER, CENTER, COUNT ETC...