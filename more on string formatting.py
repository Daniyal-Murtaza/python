# indexing in string formatting


my_name = "Daniyal"
father_name = "Anwar"



# we can either use this method:
#print("My name is {} and my father name is {} and my age is {}".format("Daniyal","Anwar","18"))



# or we can also use this method:
print("My name is {} and my father name is {} and my age is {}".format(my_name,father_name,18))




# BUT IF WE NEED TO CHANGE THE PLACES OF FORMAT PARAMETERS AS ARGUEMMENTS IN THE STRING THEN WE HAVE TO PERFORM INDEXING
#print("My name is {} and my father name is {} and my age is {}".format("Daniyal","Anwar","18"))
# places       0        1      2  now we will do indexing according to it
print("My name is {1} and my father name is {0} and my age is {2}".format("Daniyal","Anwar","18"))



# But if we need to change integers into float in the format .
number = 2
print("my number is {0:.3f}".format(number))        #if we need to round the number to certain digits then we only need to write point then number that number after colon
              # place no 0 colon f


# if the output come in 6 digits like 0.666666 it is float but if 0.666666666666 i.i greater than 6 digits is called double then if we need to round that double no to float then we will use this method
print("my number is {0:f}".format(number/3))       # but number i.e. 2/3 is 0.666666666666 that has been rounded to 0.666667



# Spacing or padding
print("my age is {0:3d}".format(22))
                  # number of digits in format + 1 shoulb be wrote with d after colon!
                   # we can also use chevron i.e. < or > to indicate the left or right where we need to add the spaces

print("my age is {0:>6}".format(22))
print("my age is {0:<6} xyz".format(22))

# we can use method of chevron in integer as well as string or float data types

# Caret symbol (^) :
print("{0:*^11s}".format("dani"))
     # if even no then equal no of asterist divide on both side while for odd 1 star would e more on the right side!

# string formatting in loops
for i in range(1,10):                       # last term do not includes in it!
    print("{} {} {}".format(i,i**2,i**3))
