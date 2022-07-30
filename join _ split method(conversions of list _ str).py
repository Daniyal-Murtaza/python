# split method --> converts string to list

# convert string to list

bio = "dani,yal,24".split(",")
print("Ans1",bio)

# splits the variables

bio,age = "daniyal,24".split(",")
print("ans2",bio)
print("ans3",age)

# join method --> converts list to string

bio = ["daniyal","24"] 
print(",".join(bio))   # lists elements should be in the strings