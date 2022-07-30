# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are 
# same from a given list of strings. 


def simsim(listioo):
    total = 0
    for i in listioo:
        if len(i) > 2 and i[0]==i[-1]:
            total += 1
    return total

print(simsim(['abc', 'xyz', 'aba', '1221',"zxxxz","22"]))