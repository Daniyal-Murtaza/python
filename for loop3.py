# Ask user name and count for each character

# LOGIC:
# username = "daniyal"     # len(username) = 7
# username.count(d) = username.count(username[0])
# username.count(a) = username.count(username[1])
# username.count(n) = username.count(username[2])
# username.count(i) = username.count(username[3])
# username.count(y) = username.count(username[4])
# username.count(a) = username.count(username[5])
# username.count(l) = username.count(username[6])


username = input("Enter user name:")
temp_var = ""
for i in range(0,len(username)):
    if username[i] not in temp_var:
        print(f"{username[i]} : {username.count(username[i])}")
        temp_var += username[i]