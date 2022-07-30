# Ask user to input 3 numbers and you to print average of these three numbers using string formatting
# bonus : Try to take all comma seperated inputs in one line

n1,n2,n3 = input("Enter n1,n2 and n3:").split(",")
Average = int(n1)+int(n2)+int(n3)/3
# for python 3:
print("The average of n1,n2 and n3 is {0:.4f}".format(Average))        # To remain the output in 4 digits after decimal
# for python 3.6:
print(f"The average of n1,n2 and n3 is {Average}")

