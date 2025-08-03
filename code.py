#Scientific Calculator
#Calculator
import tkinter as tk
import math

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Global input string
expression = ""
dark_mode = False
# Input field
input_text = tk.StringVar()

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def equal_press():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def sin():
    global expression
    try:
        result = str(math.sin(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def cos():
    global expression
    try:
        result = str(math.cos(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def tan():
    global expression
    try:
        result = str(math.tan(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def log():
    global expression
    try:
        result = str(math.log10(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def factorial():
    global expression
    try:
        result = str(math.factorial(int(float(expression))))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg_color ="#222222" if dark_mode else "#f0f0f0"
    fg_color = "#ffffff" if dark_mode else "#000000"
    btn_bg = "#333333" if dark_mode else "#ffffff"
    btn_fg = "#00ffcc" if dark_mode else "#000000"

    root.configure(bg=bg_color)
    entry.configure(bg=btn_bg, fg=fg_color)

    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.configure(bg=bg_color)
            for btn in widget.winfo_children():
                if isinstance(btn, tk.Button):
                    btn.configure(bg=btn_bg, fg=btn_fg)

# Entry field
entry = tk.Entry(root, font=('Arial', 20), textvariable=input_text, bd=10, relief="sunken", justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'sin'],
    ['1', '2', '3', '-', 'cos'],
    ['0', '.', '=', '+', 'tan'],
    ['C', '(', ')', '^', 'log'],
    ['!', '', '', '', '']
]

# Button actions
actions = {
    '=': equal_press,
    'C': clear,
    'sqrt': sqrt,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'log': log,
    '!': factorial,
    '^': lambda: press("**")
}

# Create button grid
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for char in row:
        if char == '':
            btn = tk.Label(frame, text="", width=6)
        else:
            action = actions.get(char, lambda ch=char: press(ch))
            btn = tk.Button(frame, text=char, font=('Arial', 18), command=action)
        btn.pack(side='left', expand=True, fill='both')


theme_btn = tk.Button(root, text="Toggle Theme", font=('Arial', 12), command=toggle_theme)
theme_btn.pack(pady=5)

# Start the main loop AFTER all widgets are added
root.mainloop()
