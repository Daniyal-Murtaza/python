# Check two conditions at the same time
# and / or

name = "Daniyal"
age = 19
if name == "Daniyal" and age == 18:
    print("Condition is true")
else:
    print("Condition is false")   # So we checked both the conditions at the same time!

# if you need whole condition as true in the "and" operator text then both of the conditions must be true! otherwise your else code block will be executed!

name = "Daniyal"
age = 18
if name == "Minhal" or age == 18:
    print("Condition is true")
else:
    print("Condition is false")

# if you need whole condition as true in the "or" operator text then any one of the conditions need to be true! otherwise your else code block will be executed!
