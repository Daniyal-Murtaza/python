#STRING METHODS:
#-----------------

# (1)LEN FUNCTION

# len() function is used to calculate the number of characters in the strings.
# len function also calculate space as a character . BE CAUTIOUS OF THAT.
# i.e.

name = "DaNiYaL MuRtAzA"
# we can print it as well as store it in a variable!

# For print:
print(len(name))
# For storing in variable:
length = (len(name))
print(length)

#(2)  LOWER() METHOD:
print(name.lower())              # all characters are changed into smaller case. we can also do it by assigning in variable

#(3)  UPPER() METHOD:
jj = name.upper()                # all characters are changed into bigger case!
print(jj)

#(4) TITLE() METHOD:
dd = name.title()                # Only first letter is made upper case and remaining is lower case!
print(dd)

#(5) COUNT() METHOD:
aa = name.count("A")             # since in daniyal murtaza there were 2 times a for lower case and 2 times A.
print(aa)

# LEN IS A FUNCTION AND REMAINING ARE METHOD ...THERE SYNTAX ARE DIFFERENT BE CAUTIOUS OF THAT!!!
#print(len(name))
#print(name.lower())