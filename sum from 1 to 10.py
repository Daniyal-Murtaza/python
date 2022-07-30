# sum from 1 to 10:

total = 0
for i in range (1,11):
    total += i
print(total)

# sum from 1 to n(number inputed by user):
total = 0
n = int(input("Enter number:"))
for i in range(1,n+1):    # since range function do not includes the last number so we need to do n + 1
    total += i
print(total)


