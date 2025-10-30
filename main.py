from tkinter import *
from tkinter import messagebox
import tkinter
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = [0,1,2,3,4,5,6,7,8,8,9]
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["!","@","#","$","%","^","&","*","?","+","(",")"]
password_gen = ""
def gen_pass():
    global password_gen
    for i in range (4):
        no_random = random.randint(0,9)
        alp_random = random.choice(alphabets)
        sym_random = random.choice(symbols)
        password_gen += f"{no_random}{alp_random}{sym_random}"
    password_entry.insert(tkinter.END,password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if website == "" or email=="" or password =="" :
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return
    with open("data.txt","a") as file:
        file.write(f"{website}| {email} | {password} \n")
        messagebox.showinfo("Success","Data saved successfully")
        website_entry.delete(0,tkinter.END)
        email_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text= "Email/Username:")
email_label.grid(row=2,column=0)
password_Label = Label(text= "Password:")
password_Label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"dkkamo4@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

#buttons
generate_password_button = Button(text="Generate Password",command= gen_pass)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=45,command= save_data)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()