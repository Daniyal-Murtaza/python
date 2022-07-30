def factorial(num):
    prod = 1
    for i in range(2, num+1):
        prod *= i
    return prod
    
#0! = 1!= 1 #base case
#n! = n*(n-1)!  # recursive case
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
    
print("factorial(5):",factorial(5))
print("recursive factorial(5):",fact(5))

msg='SUNDOG'
left = msg[:len(msg)//2]
right = msg[len(msg)//2:]

l_left = left[:len(left)//2]
r_left = left[len(left)//2 + 1:]

def rec_str(msg):
    if len(msg)==1:
        print(msg)
        
    else:
        #split the string
        left = msg[:len(msg)//2]
        r_len = len(msg)
        if r_len%2 !=0 :
            right = msg[r_len+1:]
        else:
            right = msg[r_len:]
        return rec_str(left) + msg + rec_str(right)
    

