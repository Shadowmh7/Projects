import tkinter as tk

# Function to update the display when a button is clicked
def button_click(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

# Function to evaluate the expression and display the result
def calculate():
    try:
        # Replace multiple symbols with their Python equivalents
        expression = display_var.get()
        expression = expression.replace('x', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('^', '**')

        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear():
    display_var.set("")

# Main application window
root = tk.Tk()
root.title("Simple Calculator")

# Display area
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),  # Use '÷' instead of '/'
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),  # Use 'x' instead of '*'
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('^', 5, 1)  # Add a button for exponentiation using '^'
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
