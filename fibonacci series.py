# fibonacci series
# 0 1 1 2 3 5 8 13 21 34

# in fibonacci series the first two terms remain constant while the proceeding terms makes the sum of previous two terms!

def fibonacci_series(n):      # n means no of terms to be included in series
    a = 0
    b = 1
    if n == 1:
        print(a) 
    elif n == 2:
        print(a, b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c = a + b
            b = c
            a = b
            print(b,end=" ")
    
(fibonacci_series(23))