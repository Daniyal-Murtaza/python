#Break And Continue Keyword

#Break: We use Break keyword to brak the loop or terminate the loop.

# if i want to print numbers from 1 to 10

for i in range(1,11):
    print(i)

# but i want to brak this loop when i approches 5 i.e. i ==5 then the syntax will be:

for i in range(1,11):
    if i ==5:
        break                   #means jab i ki value 5 hogi tou loop khud ba khud break hojaye ga!
    print(i)

# THE BEST THING ABOUT FOR LOOP WHICH DO NOT EXIST IN WHILE LOOP ARE:
# 1. CLEAN SYNTAX OF FOR LOOP
# 2. WE DON"T NEED TO GIVE THE INITIAL POINT ON SEPERATE LINE
# 3. WE ALSO DON'T NEED TO GIVE INCREMENT FORMULA ON SEPERATE LINE BECAUSE IT IS COVERED INN RANGE FUNCTION!

# Continue: If you want to print the numbers from 1 to 10 but you don't need to print 5 in it or any other certain number then conntinue keyword is used.
#i.e.

for i in range(1,11):
    if i == 5:
        continue
    print(i)

