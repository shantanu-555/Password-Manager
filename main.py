from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(bg="#f0f0f0", padx=20, pady=20)  # Added background color and padding

# Create and place the logo
canvas = Canvas(window, height=200, width=200, bg="#f0f0f0", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=10)  # Adjusted columnspan and added padding

# Labels
labels = ["Website:", "Email/Username:", "Password:"]
for i, text in enumerate(labels):
    label = Label(window, text=text, font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i+1, column=0, sticky="e", padx=5, pady=5)

# Entries
website_entry = Entry(window, width=36, font=("Arial", 12))
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)
website_entry.focus()

email_entry = Entry(window, width=36, font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=5)

password_entry = Entry(window, width=20, font=("Arial", 12))
password_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

# Buttons
generate_password_button = Button(window, width=15, text="Generate Password", command=generate_password, font=("Arial", 10), bg="#4CAF50", fg="white", relief="raised")
generate_password_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")

add_button = Button(window, text="Add", width=25, command=add_password, font=("Arial", 12), bg="#008CBA", fg="white", relief="raised")
add_button.grid(row=4, column=0, columnspan=4, pady=10)

window.mainloop()