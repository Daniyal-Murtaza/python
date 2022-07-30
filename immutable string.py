# strings are immutable means once you have made the string then it cannot be changed!
name = "daniyal"
print(name[1])             # it prints the first character i.e.  "a"

# but now once the string has been made we cannot interchange this a with upper case or any other characte i.e. name[1] isnot equal to A
# but we can say that we can do it by replace method i.e

print(name.replace("a","A"))
print(name)

# looking at the output what is happening?? 
# replace method is actually used to form the new string by replacing the characters mentioned in the string i.e. it do not alters the original string but form a new string with given conditions.
