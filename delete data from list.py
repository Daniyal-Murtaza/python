# method to delete form the list

listie = ["orange","apple","pear","banana","kiwi"]

# (1) pop method --> deletes last element of the list

listie = ["orange","apple","pear","banana","kiwi"]
listie.pop()
print("ans1",listie)

#we can give argguement in the pop to delete the specific element of the list

listie = ["orange","apple","pear","banana","kiwi"]
listie.pop(2)
print("ans2",listie)

# (2) delete statement or operator [del] --> deletes that element that we have specified the index for

listie = ["orange","apple","pear","banana","kiwi"]
del listie[0:2]
print("ans3",listie)

# (3) remove method --> removes the element from the list , used when you donot know the indexing

listie = ["orange","apple","pear","banana","kiwi"]
listie.remove("apple")
print("ans4",listie)

# but if there are two apples in the list then it will only delete the first one

#SUMMARIZE

# To add elements in the list : append, extend, insert
# to delete elements form the list: pop, remove, del