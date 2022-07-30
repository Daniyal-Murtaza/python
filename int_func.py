# Since input function takes the input from the user as the string data type si it didn't add but simply concatenate!

#first_number = input("Enter first number:")
#second_number = input("Enter second number:")
#total = first_number + second_number
#print("Total is"+total)

# But if we need to add both the string data type that we take from the user than:

first_number = int(input("Enter first number:"))    # 4
second_number = int(input("Enter second number:"))   # 4
total  = first_number+second_number                  # 8
print("Total is:" + str(total))                      # but 8 is an int and here "Total is" is in string data type therefore 
                                                    #we are also changing total in string form as
# if we take the sum of the integer data type and float data type then the answer will be in the float data type!