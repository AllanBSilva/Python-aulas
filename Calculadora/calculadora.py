import tkinter as tk

def press_key(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("270x240")

# Entry widget to display input and output
entry = tk.Entry(window, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry2 = tk.Entry(window, width=40, borderwidth=5)
entry2.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_index = 2
col_index = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=5, command=calculate).grid(row=row_index, column=col_index, columnspan=1, padx=5, pady=5)
    elif button == 'C':
        tk.Button(window, text=button, width=5, command=clear).grid(row=row_index, column=col_index, columnspan=1, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=5, command=lambda key=button: press_key(key)).grid(row=row_index, column=col_index, padx=5, pady=5)
    
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

window.mainloop()