# Bubble sort algorithm:

# It will bubble up the greatest one to the correct location after each iteration

lst = [10,2,1,9,5]

def bubblesort(lst):
    for i in range(len(lst)):                                             # len(lst) = 7 means 7 iterations
        for j in range(0,len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst
        
print(bubblesort(lst))
        
    