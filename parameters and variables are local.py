# parameters and variables are local means if it is used insiide the body of the function then it will no longer exist if the
# function terminates i.e. 


def name_twice(first_name,last_name):
    name = first_name+last_name
    print(name)
name_twice("daniyal","murtaza")

# parmeters are also local becauz there exist no such thing as first_name and last_name besides function