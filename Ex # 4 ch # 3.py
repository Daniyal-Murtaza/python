# Exercise:
# Ask user to input a number containing more than one digit i.e. 1256
# Calculate 1+2+5+6 and print

#HINTS:
# Algorithm (method to solve problem in human language)
# Ask input in string i.e. don't change string to int
# example "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example[1]) ... go upto len(example)

number = input("Enter number:")
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)