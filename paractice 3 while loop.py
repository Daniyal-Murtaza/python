#Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
#4! = 1*2*3*4 = 24
#3! = 3*2*1 = 6
#2! = 2*1 = 2
#Also,
#1! = 1
#0! = 1
#Write a program to calculate factorial of a number.

total = 1
i = 1
factorial_number = int(input("Enter number:"))

if factorial_number == 0:
    print(1)

else:
    while factorial_number >=1:
        factorial_number *= 1
        total *= factorial_number
        factorial_number -= 1
    print(total) 
    


