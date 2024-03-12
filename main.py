import ttkbootstrap as ttk
from tkinter import END,messagebox
import random
import pandas
import string

printables = list(string.ascii_letters+string.digits+ string.punctuation)
print(printables)
random.shuffle(printables)
print(printables)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Password_generator():
    password = ''.join(random.choices(printables,k=16))
    password.strip()
    Password_var.set(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    email = EmailEntry.get()
    password = PasswordEntry.get()
    website = WebsiteEntry.get()
    data = pandas.read_csv("Password_data.csv")
    if messagebox.askyesno('Confirmation' ,message= f" Website : {website} \n Email = {email} \n Password: {password}\n Is being added to the Data file"):
        new_row = {'website': website, 'email': email, 'password': password}
        data = pandas.concat([data, pandas.DataFrame([new_row])], ignore_index=True)
        data.to_csv("Password_data.csv",index=False)
        WebsiteEntry.delete(0,END)
        PasswordEntry.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = ttk.Window(title="Password Manager",themename='darkly')
window.config(padx=50,pady=20)

#Variables
Password_var = ttk.StringVar(value="")

#CANVAS SETUP 

canvas = ttk.Canvas(width= 300 , height= 200)
image = ttk.PhotoImage(file="logo.png")
canvas.create_image(150,100,image=image)
canvas.grid(column=1, row=0)

#Website Entry 

labelWebsite = ttk.Label(text="Website" , font= ("calibri",10,"normal"))
labelWebsite.grid(column=0,row=1,padx=20,pady=10)

WebsiteEntry = ttk.Entry(width=45)
WebsiteEntry.focus()
WebsiteEntry.grid(column=1,row=1,columnspan=3,padx=20,pady=10 ,sticky='w')

#Email Entry


labelemail = ttk.Label(text="Email" , font= ("calibri",10,"normal"))
labelemail.grid(column=0,row=2,padx=20,pady=10)

EmailEntry = ttk.Entry(width=45)
EmailEntry.insert(0,"Howatabik@gmail.com")
EmailEntry.grid(column=1,row=2,columnspan=3,padx=20,pady=10,sticky='w')

#Password Entry

labelPassword = ttk.Label(text="Password" , font= ("calibri",10,"normal"))
labelPassword.grid(column=0,row=3,padx=20,pady=10)

PasswordEntry = ttk.Entry(width=35,textvariable=Password_var)
PasswordEntry.grid(column=1,row=3,padx=22,pady=10,sticky='w',columnspan=2)

PasswordGen_button = ttk.Button(text="Generate",command=Password_generator)
PasswordGen_button.grid(column=2, row = 3,sticky='e')



AddButton = ttk.Button(text="Add" , width=10 , command=add_button)
AddButton.grid(column=1, row = 4 ,pady=20)


window.mainloop()