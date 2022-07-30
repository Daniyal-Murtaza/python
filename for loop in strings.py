# for printing all the words of the string we have learned the syntax in previous videos that:
# this is the long way and works in all programming languages!

name = "daniyal"
for i in range(len(name)):
    print(name[i])

# given below method is for python!
name = "daniyal"
for i in name :   # we can also replace variable by string as well!
    print(i)

# now lets make a program for it!
# input a number and sum it

sum = input("Enter a number:")
total =0
for i in sum:
    total += int(i)
print(total)    


