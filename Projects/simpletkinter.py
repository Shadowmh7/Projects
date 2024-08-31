import tkinter as tk

def clear_entry(event, entry):
    entry.delete(0, tk.END)
    entry.config(fg='black')

def create_entry_with_placeholder(root, placeholder, width=20):
    entry = tk.Entry(root, width=width, fg='grey')
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: clear_entry(event, entry))
    return entry

# Create the main window
root = tk.Tk()
root.title("User Information")

# Create a frame for each row
frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

# Create and place 'Name' Entry with placeholder and Label
name_entry = create_entry_with_placeholder(frame1, "Enter your name")
name_entry.pack(side=tk.LEFT)

name_label = tk.Label(frame1, text="Name:")
name_label.pack(side=tk.RIGHT)

# Create and place 'Age' Entry with placeholder and Label
age_entry = create_entry_with_placeholder(frame2, "Enter your age")
age_entry.pack(side=tk.LEFT)

age_label = tk.Label(frame2, text="Age:")
age_label.pack(side=tk.RIGHT)

# Start the Tkinter main loop
root.mainloop()
