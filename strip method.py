# STRIP IS A METHOD! NOT A FUNCTION! AND METHOD HAVE SAME SYNTAX I.E.  variable.methodname() =>  name.strip()

name = "    Dani    yal    "
text = "......."
print(name+text)             #    Dan    iyal    .......      it's output

# in ordre to remove these spaces we will use strip method.

# for removing left hand spaces.
print(name.lstrip()+text)
                                                                        
# for removing right hand spaces
print(name.rstrip()+text)

# for removing both left and right hand spaces
print(name.strip()+text)

#but the strip method is only used to remove left or right or both spaces. now if the syntax of variable is like this
# |    dani    yal     |. by the help of strip we can remove left and right spaces but in order to remove the spaces in between
# the variable then we have to use replace method.

# Remember replace is also the method so now u have the syntax in mind

print(name.replace(" ","")+text)    #Here we have replaced spaces with i.e. " " with no spaces i.e ""



