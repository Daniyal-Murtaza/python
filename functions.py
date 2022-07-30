# We have used function previously without being known that we are actually using functions like len function which gives the length of the string.
# But those are built in functions of the python.

#USER DEFINED FUNCTIONS:
#-----------------------

# We use def keyword to define our own function
# i.e. Write a program to sum any two numbers:

def add_two(a,b):
    return a+b

print(add_two(5,7))
print(add_two(10,40))

# For integers!
num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
print(add_two(num1,num2))

#For strings!
first_name = input("Enter first name:")
second_name = input("Enter second name:")
print(add_two(first_name,second_name))

# Hence function have prevented us from doing the same thing again and again!