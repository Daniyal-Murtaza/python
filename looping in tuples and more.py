# looping in tuple --> same as others

name = ("daniyal","minhal","jamal","hasnain")
for i in name:
    print("ans1",i)
    
# tuple with one element --> need to add , after one and only element

name = (1)
print(type(name))  # int type

name = (1,)
print(type(name))  # tuple type

name = ("daniyal",)
print(type(name))  # tuple type

name = ("daniyal")
print(type(name))  # string type

# tuple without paranthesis

name = "daniyal","minhal",111,0.111,None
print(type(name))  # tuple data type

# tuple unpacking

name = ("daniyal","minhal","hasnain","jamal")
name1,name2,name3,name4 = (name)
print("ans2",name1)
print("ans2",name2)

# list inside tuple

dattebayo = ("daniyal",[1,2,3])
print("ans3",dattebayo[1])

dattebayo[1][1] = 5
print("ans4",dattebayo)

dattebayo[1].pop()
print("ans5",dattebayo)

dattebayo[1].append(4)
print("ans6",dattebayo) 

# we can apply all the methods on the list inside the tuple


# we can apply min(),max(),sum()
naruto = (1,33,2,66)
print(sum(naruto))
print(min(naruto))
print(max(naruto))

# tuples returning two values

def mulsum(n,f):
    jj = n + f
    kk = n * f
    return jj,kk    # it will return a tuple

print(mulsum(2,3))








