#Ask user name and print back user name in reverse order
# BONUS: Try to make your program in 2 lines using string formatting:

username = input("Enter your username:")
print(username[-1:-8:-1])
#or
print(username[-1::-1])
# for python 3.6
print(f"reverse of your name is{username[-1::-1]}")
# for python 3
print("reverse of your name is {}".format(username[-1::-1])) 