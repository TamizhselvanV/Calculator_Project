import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("350x500")
root.config(bg="#f4f4f4")

expression = ""

# Update the input field
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Backspace
def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Evaluate the expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Text input field
input_text = tk.StringVar()

entry = tk.Entry(root, font=('arial', 24, 'bold'), textvariable=input_text, bd=12, insertwidth=4,
                 bg="#111", fg="#0f0", justify='right')
entry.grid(columnspan=4, ipadx=8, ipady=15, pady=10)

# Button layout
buttons = [
    ('C', 1, 0, 'red', clear),
    ('⌫', 1, 1, 'purple', backspace),
    ('%', 1, 2, 'orange', lambda: press('%')),
    ('÷', 1, 3, 'orange', lambda: press('/')),

    ('7', 2, 0, None, lambda: press('7')),
    ('8', 2, 1, None, lambda: press('8')),
    ('9', 2, 2, None, lambda: press('9')),
    ('×', 2, 3, 'orange', lambda: press('*')),

    ('4', 3, 0, None, lambda: press('4')),
    ('5', 3, 1, None, lambda: press('5')),
    ('6', 3, 2, None, lambda: press('6')),
    ('−', 3, 3, 'orange', lambda: press('-')),

    ('1', 4, 0, None, lambda: press('1')),
    ('2', 4, 1, None, lambda: press('2')),
    ('3', 4, 2, None, lambda: press('3')),
    ('+', 4, 3, 'orange', lambda: press('+')),

    ('0', 5, 0, None, lambda: press('0')),
    ('.', 5, 1, None, lambda: press('.')),
    ('=', 5, 2, 'green', equalpress),
]

# Add buttons to the window
for (text, row, col, color, cmd) in buttons:
    btn = tk.Button(root, text=text, padx=20, pady=20, bd=4,
                    font=('Arial', 14, 'bold'), command=cmd)
    if color:
        btn.config(bg=color, fg='white')
    else:
        btn.config(bg='#eee')
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Make = span two columns
tk.Button(root, text='=', padx=20, pady=20, bd=4,
          font=('Arial', 14, 'bold'), bg='green', fg='white',
          command=equalpress).grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky='nsew')

root.mainloop()
