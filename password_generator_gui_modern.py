import string
import secrets
import re
import pyperclip
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        label = label_entry.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        # Ensure at least one character of each selected type
        password = []
        if use_letters:
            password.append(secrets.choice(string.ascii_letters))
        if use_numbers:
            password.append(secrets.choice(string.digits))
        if use_symbols:
            password.append(secrets.choice(string.punctuation))

        while len(password) < length:
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)
        password_str = ''.join(password)

        # Display password
        password_var.set(password_str)
        pyperclip.copy(password_str)

        # Check strength
        strength, color = check_strength(password_str)
        strength_label.config(text=f"Strength: {strength}", fg=color)

        # Save to file
        with open("passwords.txt", "a") as f:
            f.write(f"{label}: {password_str}\n")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length.")

# Check password strength with color coding
def check_strength(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return "Strong", "green"
    elif len(password) >= 6:
        return "Moderate", "orange"
    else:
        return "Weak", "red"

# Toggle password visibility
def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show='')
        toggle_btn.config(text="Hide")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Frame for inputs
frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame.pack(pady=10)

# Length
tk.Label(frame, text="Password Length:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, pady=5)

# Checkboxes
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Include Letters", variable=letters_var, bg="#f0f0f0").grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").grid(row=1, column=1, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").grid(row=2, column=0, sticky="w")

# Label
tk.Label(frame, text="Password Label:", bg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=(10,0))
label_entry = tk.Entry(frame, width=20)
label_entry.grid(row=3, column=1, pady=(10,0))

# Generate button
tk.Button(frame, text="Generate Password", bg="#4CAF50", fg="white", command=generate_password).grid(row=4, column=0, columnspan=2, pady=15)

# Password display with show/hide
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=40, font=("Arial", 12))
password_entry.pack(pady=5)

toggle_btn = tk.Button(root, text="Show", command=toggle_password)
toggle_btn.pack(pady=5)

# Strength label
strength_label = tk.Label(root, text="Strength: ", bg="#f0f0f0", font=("Arial", 10, "bold"))
strength_label.pack(pady=5)

root.mainloop()
