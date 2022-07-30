# To generate list from range function

numbers = list(range(1,20))
print(numbers)

# pop method returns the value as well

listie = [1,2,3,4,5,6,7,8,9]
print(listie.pop())

# index method --> to get the index of any item

listie = [1,2,3,4,5,6,7,8,9]
print(listie.index(3))

# we can specify position to start the search operation and end

listie = [1,2,3,4,5,6,7,8,9,1]
print(listie.index(1,2,8))