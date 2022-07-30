# list
# data structure
# ordered collection of items
# we can store int, float, list, int etc

numbers = [1,2,3,4,5]
print("ans1",numbers)

words = ["word1","word2","word3"]
print("ans2",words)

mixed = [1,2,3,"daniyal","murtaza",0.003,None]
print("ans3",mixed)

# to acess data

mixed = [1,2,3,"daniyal","murtaza",0.003,None]
print("ans4",mixed[3])
print("ans5",mixed[3:-1])

# to modify data in the list

mixed = [1,2,3,"daniyal","murtaza",0.003,None]
mixed[3] = "jamal"
print("ans6",mixed)

# to modify data to split the words in the string and then store it

mixed[2:-2] = "top"
print("ans7",mixed)

# to modify data to add the words of the list in the initial list

mixed[2:-2] = ["yoyo","jaja","kaka","hoho"]
print("ans8",mixed)

# we can do ans7 by this method as well

mixed[2:-2] = ["t","o","p"]
print("ans9",mixed)

# ans 7,8,9 ka matlab ye hai k given indices k darmian given list ya given string add krdo lekin string khud hi split hokr add hogi 
