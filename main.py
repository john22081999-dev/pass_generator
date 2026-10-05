from tkinter import*
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    psw.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = website.get()
    email_entry = email.get()
    password = psw.get()

    if len(website_entry) == 0 or len(password) == 0 or len(email_entry) == 0:
        messagebox.showwarning(title="Warning" ,message="Some field have not been entered")
    else:
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"These are the details entered: \nEmail: {email_entry} \nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{website_entry} | {email_entry} | {password}\n")
            # Empty after save
            website.delete(0, END)
            email.delete(0, END)
            psw.delete(0, END )

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(height=200, width=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0, columnspan=3)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="E")

psw_label = Label(text="Password:")
psw_label.grid(column=0, row=3, sticky="E")

# entries
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
website.focus()

email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "example@gmail.com")

psw = Entry(width=21)
psw.grid(column=1, row=3)


#buttons
generate_psw = Button(text="Generate Password", command=password_generate)
generate_psw.grid(column=2, row=3)

add = Button(text="Add", command=save ,width=36)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()