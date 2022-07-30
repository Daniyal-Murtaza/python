# define your function to take two parameters as the input and it returns which parameter is greater 

def greater(num1,num2):
    if num1 > num2:
        return num1
    
    elif num2 > num1:
        return num2

    else:
        return "They are equal!"

print(greater(22,33))
print(greater(2,2))

# in order to find the greatest1

def greatest(a,b,c):
    if a> b and a>c :
        return a
    if b> a and b>c :
        return b
    if c> a and c>b :
        return c

print(greatest(10,20,30))


# function inside function:
# greater(a,b)----> a or b
# greater(a or b,c)----> greatest

def new_greatest(a,b,c):
    #bigger = greater(a,b)
    return (greater(greater(a,b),c))   # we should strive to complete our code in as minimum lines as possible!

print(new_greatest(10,50,1000))

# PROGRAMMING PRINCIPLE KISS: KEEP IT SIMPLE STUPID! but we it's our choice if we need to take our code to multiple lines or just 1 line!
