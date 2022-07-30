# There are 3 elements in the given below list

listie = [[1,2,3],[4,5,6],[7,8,9]]
print("ans1",listie[1])

# To print sublist in the list:

for sublist in listie:
    print("ans2",sublist)
    
# To print the elements of sublist

for sublist in listie:
    for elements in sublist:
        print("ans3",elements)
        
# to access 5 what should we do?

listie = [[1,2,3],[4,5,6],[7,8,9]]
print("ans4",listie[1][1])

print(type(listie))


