# for use krte hoai range function mai step dalna step arguement in range function kehlata hai!
#i.e.

for i in range (1,11):        # it is just a simple syntax but there's a hidden syntax in it i.e. (1,11,1) 1 is step,which we don't need to write
    print(i) 

# for 2 steps taken between the specified range. 

for i in range (1,11,2):
    print(i)

# This program is specialized for printing odd or even numbers!

# if we wnat to print bbackwards range then the syntax will be:

for i in reversed(range(1,10)):
    print(i)

# we can also print backeards like this method:

for i in range(10,0,-1):
    print(i)