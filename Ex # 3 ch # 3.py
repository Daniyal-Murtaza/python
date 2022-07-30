# sum of n natural numbers
# ask a user for natural number (n)
# print total from 1 to n

n = int(input("Enter natural number:"))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)