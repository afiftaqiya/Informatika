# make gui of calculator in python
import tkinter as tk

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=10, command=calculate)
    elif button == "0":
        btn = tk.Button(root, text=button, width=10, command=lambda: entry.insert(tk.END, "0"))
    else:
        btn = tk.Button(root, text=button, width=10, command=lambda button=button: entry.insert(tk.END, button))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_btn = tk.Button(root, text="C", width=10, command=clear)
clear_btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
