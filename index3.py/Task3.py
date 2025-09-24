#Task3

import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            result.set("Length > 0 required")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result.set(password)
    except:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14), wraplength=350).pack(pady=10)

root.mainloop()