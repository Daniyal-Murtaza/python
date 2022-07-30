# These two lines are must
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

# It is used to give name to your GUI
root.title("GUI")

# to use label in your created window
name_label = ttk.Label(root, text = "Enter your name :")
name_label.grid(row = 0, column=0 , sticky=tk.W)

email_label = ttk.Label(root, text = "Enter your email :")
email_label.grid(row = 1, column = 0, sticky=tk.W)

age_label = ttk.Label(root, text = "Enter your age :" )
age_label.grid(row = 2, column = 0, sticky=tk.W)

gender_label = ttk.Label(root, text = "Select your gender :" )
gender_label.grid(row = 3, column = 0, sticky=tk.W)

# location should added
# location : grid , pack 

# To make entry box where user will give their answer "Entry box"
# to store the user name we will make a variable

name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width= 35, textvariable = name_var)
name_entrybox.grid(row=0 , column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(root, width= 35, textvariable = email_var)
email_entrybox.grid(row=1 , column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(root, width= 35, textvariable = age_var)
age_entrybox.grid(row=2 , column=1)

# To create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, width = 32, textvariable = gender_var, state = "readonly")
gender_combobox["value"] = ("Male" , "Female", "Others")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# To create radio button
#teacher, student

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(root, text = "Student", value="Student", variable= usertype)
radiobtn1.grid(row=4, column= 0)

radiobtn2 = ttk.Radiobutton(root, text = "Teacher", value="Teacher", variable= usertype)
radiobtn2.grid(row=4, column= 1)

# check button:

checkbtn_var =tk.IntVar()
checkbtn = ttk.Checkbutton(root, text ="Check if you want to subscribe to our newsletter", variable = checkbtn_var)
checkbtn.grid(row=5 , columnspan=3)



#To create button:
#And after creating button we need button to perform some action : {command = action}

def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f"{username} is {userage} years old, {user_email}")
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0 :
        subscribed = "No"
    else:
        subscribed = "Yes"
    print(user_gender, user_type, subscribed)
    
    with open("file.txt","a") as f:
        f.write(f"{username},{userage},{user_email},{user_gender},{user_type},{subscribed}\n")
        
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    
    # To change colour of labels
    name_label.configure(foreground="Blue")
    
submit_button = ttk.Button(root, text = "submit" , command =  action )
submit_button.grid(row = 6, column = 0 ,  sticky= tk.W )







# This need to written after every ending the tinker program
root.mainloop()             