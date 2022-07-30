# strings
# collection of characters inside single quote or double quote

# string concatenation means to add the data type of string 
#i.e.

first_name = "Daniyal"
last_name = "Murtaza"
full_name = first_name+last_name
print(full_name)                          # this is called string concatenation

# we can only concate strings with the strings but cannot concate strings with the integer or any other data type but first we need
# to change data types into the same then proceed with the concate process
# i.e.

#print(full_name+3)         # it will give error becauz one data type is string and other is int

# now we are changing it to same adata types
print(first_name + "4")
#or we can also do
print(first_name + str(4))

# we can also print first name three times
print(first_name * 4)