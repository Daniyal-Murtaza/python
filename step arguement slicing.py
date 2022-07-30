# we have learned the concept of printing only character of given variable or printing certain range of that character but if we want to atep the arguements in between like daniyal and i only want to print d n y  then :
name = "daniyal"
print(name[0:5:2]) # here 0 specify initaial point of range and 5 specify final-1 [oint of range while 2 specify to step the arguement character in between!]
 
 # while if we 1 as a step then it will not step any writing but only perform slicing!
print(name[0:5:1])

print(name[::2])
print(name[:4:2])
print(name[2::3])

# in order to reverse the string
print(name[-1::-1])
print(name[::-1])