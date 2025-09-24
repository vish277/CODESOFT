#task 2

import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error (Div by 0)")
        else:
            result.set("Invalid Op")
    except:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

operation = tk.StringVar()
operation.set("+")

tk.OptionMenu(root, operation, "+", "-", "*", "/").pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack(pady=10)

root.mainloop()