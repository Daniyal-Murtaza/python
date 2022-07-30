s = input("Enter name:")
def right_justify(s):
    var = ""
    space = " " * 70
    var += space
    var += s
    return(var)
print(right_justify(s))