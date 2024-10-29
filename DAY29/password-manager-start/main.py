from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",message="Please fill in all entries")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are the following details correct?\n"
                                                      f"Email: {email} \nPassword: {password}")
        if is_ok:
            with open("data.txt",'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady= 50,padx= 50)

canvas = Canvas(height=200,width=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= pass_image)
canvas.grid(row= 0, column= 1)


website_label = Label(text="Website:")
website_label.grid(row= 1, column= 0)

website_entry = Entry()
website_entry.grid(row= 1, column=1, columnspan=2, sticky="EW")
website_entry.focus()


email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0,"tarush2004@gmail.com")


password_label = Label(text="Password:")
password_label.grid(row=3, column= 0)

password_entry = Entry()
password_entry.grid(row=3,column=1, sticky="EW")

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3, column=2)


add_button = Button(text="Add",command=save)
add_button.grid(row= 4, column=1, columnspan=2, sticky="EW")






window.mainloop()