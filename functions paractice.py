# Define your function to print last character of any name:

def last_character(name):
    return name[-1]
print(last_character("murtaza"))

# Define your function to identify taht either the number is even or odd:

def even_or_odd(number):
    number = int(number)
    if number % 2 == 0 :
        return "number is even!"

    elif number % 3 == 0:
        return "number is odd!"

    elif number % 2 == 0 and number % 3 == 0:
        return  "Even as well as odd!"

    else:
        return "none!"

print(even_or_odd(4))

# or

def is_even(num):
    if num % 2 == 0:
        return True
    
    else:
        return False

print(is_even(4))

# or 

def even(numb):
    return numb % 2 == 0

print(even(10))