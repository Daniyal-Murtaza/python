# Ask user a number like 1256
# calculate sum of these digits i.e. 1+2+5+6
# num ="1256"
# len(num)
# num[0] = 1
# num[1] = 2
# num[2] = 5
# num[3] = 6

number = input("Enter number:")
total = 0

for i in range(0,len(number)):
    total += int(number[i])
print(total)