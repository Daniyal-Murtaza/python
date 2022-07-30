
no = input("enter no:")
x = input("enter x:")
def square(x):
    return x*x
def express(no):
    sum = 0
    for i in range(1,no+1):
        squared_value = square(i)
        sum += squared_value
    return sum

print(express(no))

    