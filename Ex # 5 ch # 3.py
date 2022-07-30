# ask a user for name
# Example:  Daniyal 
# print count of each word



name = input("Enter name:")

# daniyal   
# name.count("d") , name.count(name[0])
# name.count("a") , name.count(name[1])
# name.count("n") , name.count(name[2])
# name.count("i") , name.count(name[3])
# name.count("y") , name.count(name[4])
# name.count("a") , name.count(name[5])
# name.count("l") , name.count(name[6])

# output should come in that format!
# d : 1 
# same for all words

var = ""
i = 0
while i < len(name):
    if name[i] not in var:
        var += name[i] 
        print(f"{name[i]}: {name.count(name[i])}")
    i += 1



