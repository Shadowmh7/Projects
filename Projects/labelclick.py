import tkinter as tk

def on_click():
    button.config(text="Button Clicked!")

# Main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=10)

# Button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Run the application
root.mainloop()
