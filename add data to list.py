# how to add items to our list

# (1) append method --> adds data in the last.

empty = []
fruits = ["melon","apple","banana"]
fruits.append("grapes")
fruits.append("pomogerenate")
empty.append(1)
print("ans1",fruits)
print("ans2",empty)

# append method can only add one item at a time

# (2) Insert method--> adds data in the specified position

brothers = ["jamal","minhal","hasnain"]
brothers.insert(2,"daniyal")
print("ans3",brothers)

# (3) To concatenate two lists

emm = []
fruits = ["melon","apple","banana"]
brothers = ["jamal","minhal","hasnain"]
concatenate = fruits + brothers
emm +=fruits
print("ans4",concatenate)
print("ans5", emm)

# (4) extend method --> to  add brothers list in the end of fruits list

fruits = ["melon","apple","banana"]
brothers = ["jamal","minhal","hasnain"]
fruits.extend(brothers)
print("ans6",fruits)

# what if we repest the above process but with the append method

fruits = ["melon","apple","banana"]
brothers = ["jamal","minhal","hasnain"]
fruits.append(brothers)
print("ans7",fruits)

# That is the difference between the extend and append
