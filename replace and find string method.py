#Replace method

python = "hello daniyal! nice to meet you to u"
# if i want to replace all spaces by underscores then we can use REPLACE METHOD
print(python.replace(" ","_"))

#we can also replace alphabeets or words with the replace method! (both to will be replaced by too)
print(python.replace("to","too"))

# but if i want to replace "to" which comes on first position then i have to specify it's position as well.
# python = "hello daniyal! nice to meet you to u"
#                           #1st pos      #2nd pos

print(python.replace("to","too",1))       # first one will removed by too
print(python.replace("to","too",2))       # both will removed by too
print(python.replace("to","too",3))       # still both will remove by too

#find method:

# it is used to determine the position of character in the string
#if i want to know the position of 1st position "to" then:

print(python.find("to"))

#if i want to know the position of 2nd position to then first i have to find the position of 1st position "is" then we will be able to find the position of 2nd position "is".
to_pos1 = python.find("to")
to_pos2 = python.find("to",to_pos1+1)
print(to_pos2)