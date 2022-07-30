# if elif else statement!
# if we were to verify multiple conditions then we use these statements!

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = input("Enter your age:")
age = int(age)

if age<=0:
    print("you aren't born yet! patience!")

elif 0<age<=3 :
    print("Ticket fee: free")

elif 3<age<=10:
    print("Ticket fee: 150")

elif 10<age<=60:
    print("Ticket fee: 250")

else:
    print("Ticket fee: 200")
