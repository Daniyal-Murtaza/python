# Take two comma seperated input from the user
#1) user's name
#2) a single character

# output - 2 print lines
#1) user's name length
#2) count the character that user inputed   (BONUS: Case insensitive count)

user_name, single_character = input("Enter user name and single character:").split(",")
print(f"length of user name is: {len(user_name)}")

# CASE INSENSITIVE: "Treating upper and lowercase letters as being the same"

# for sensitive case:                      
# If the input by the user is in spaces like     daniyal  then first we will use strip  i.e.   name.strip() and single_character.strip()                             
# change user_name into smaller case by : user_name.lower()
# change single character into smaller case as well by : single_character.lower()
# now we have to count the single inputed character from the name by : user_name.strip().lower().count(single_character.lower())

print(f"character count:{user_name.strip().lower().count(single_character.strip().lower())}")


