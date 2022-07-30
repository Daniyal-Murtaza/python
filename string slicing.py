# in string indexing we learned how we can print only 1 digit of the given variable but if we want to print half variable that's where string slicing or selecting sub sequences come like a super man!

lang = "python"
# for string indexing the syntax was print(variable in which value is stored[index no.])
# for string slicing the syntax is print(variable in which value is stored[you will specify range of index]) i.e start arguement and the stop arguement

# if we only need to print phy from python
print(lang[0:3])    #last index no. in this case 3 is not printed!

# for th in python
print(lang[2:4])

# for n in python
print(lang[-1])

# for pytho from python:
print(lang[0:5])

# but if do not give the stop arguement then it will itself go to the last given arguement in the variable
print(lang[0:]) 
print(lang[2:])

# and if do not give the start arguement then it will go n-1 of stop arguement
print(lang[:2])