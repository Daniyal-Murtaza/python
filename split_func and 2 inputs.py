#name , age = input("Enyer your name and age").split()     # we can replace it by comma as well
#print(name)
#print(age)

name, age = input("Enter your name and age").split(",")     # but then we have to use comma in output as well as character between two outputs in quotations marks
print(name)
print(age)



b = "hammad abdul razzaq"
a = b.split()
first_name = a[0]
last_name = a[-1]
first_name_first_character = first_name[0]   #b.split()[0][1]
last_name_first_character = last_name[0]
