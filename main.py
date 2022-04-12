from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LIGHT_BLUE = "#008E89"
FONT = ("arial", 10, "bold")
# ____________________________________________PASSWORD GENERATOR___________________________________________


def password_generation():
    password_entry.delete(0, END)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    character = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    num_alpha = random.randint(8, 10)
    num_num = random.randint(2, 4)
    num_char = random.randint(2, 4)

    password_alpha = [random.choice(alphabet) for _ in range(num_alpha)]
    password_num = [random.choice(number) for _ in range(num_num)]
    password_char = [random.choice(character) for _ in range(num_char)]

    password = password_alpha + password_num + password_char
    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ______________________________________________SAVE PASSWORD______________________________________________
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    dic = {"website": website, "email": email, "password": password}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="OOPS>>", message="Please don't leave any field empty")
    else:
        messagebox.askokcancel(title=website, message=f"These are the details entered:\n email: {email}\n password: "
                                                      f"{password}\n is it ok to save ?")
        with open("data.txt", mode='a') as data:
            for i in dic:
                data.write(f"{i} : {dic[i]} \n")
            data.write("\n\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ________________________________________________UI DESIGN________________________________________________

display = Tk()
display.title("Password Manager ~ Satya Bhusan Prusty")
display.config(padx=50, pady=50, bg=LIGHT_BLUE)

canvas = Canvas(width=200, height=200, bg=LIGHT_BLUE, highlightthickness=0)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1, sticky='w')

# Labels

label_1 = Label()
label_1.config(text="Website:", bg=LIGHT_BLUE, font=FONT)
label_1.grid(row=1, column=0, sticky='w')

label_2 = Label()
label_2.config(text="Email/Username:", bg=LIGHT_BLUE, font=FONT)
label_2.grid(row=2, column=0, sticky='w')

label_3 = Label()
label_3.config(text="Password:", bg=LIGHT_BLUE, font=FONT)
label_3.grid(row=3, column=0, sticky='w')

# Entry
website_entry = Entry(width=43)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')
email_entry.insert(0, "abc@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1, sticky='w')

# Button
generate_password_button = Button()
generate_password_button.config(text="Generate Password:", borderwidth=1, width=16, command=password_generation)
generate_password_button.grid(row=3, column=1, sticky='e', columnspan=2)

add_button = Button()
add_button.config(text="Add", width=36, borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

display.mainloop()
