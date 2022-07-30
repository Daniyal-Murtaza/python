# count method --> to count the number of times a specific element repeats in a list

fruits = ["banana","kiwi","melon","kiwi"]
print("ans1",fruits.count("kiwi"))


# sort method --> to sort the list with respect to alphabetical order or integers but you need to print the list variable in the end

fruits = ["banana","kiwi","melon","kiwi"]
fruits.sort()
print("ans2",fruits)

numbers = [2,644,23,1,33]
numbers.sort()
print("ans3",numbers)

# sorted function --> In this, you do not need to print the list variable in the end

numbers = [266,1,364,0,23]
print(sorted(numbers)) # ans4

# clear method --> it will empty the list by deleting it's elements

yum = [2,644,"daniyal",[0,2]]
yum.clear()
print("ans5",yum)

# copy method --> copies the variable list

yum.copy()
print("ans6",yum)

# reverse method --> reverses the list

numbers = [266,1,364,0,23]
numbers.reverse()
print("ans7",numbers)



