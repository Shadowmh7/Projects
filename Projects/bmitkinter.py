import tkinter as tk
from tkinter import ttk

def calculate():
    height_input = entry_input.get()
    weight_input = entry2_input.get()
    
    try:
        height = float(height_input)
        weight = float(weight_input)
        bmi = get_bmi(height, weight)
        output_input.set(bmi)
    except ValueError:
        output_input.set("Please enter valid numbers.")

def get_bmi(height, weight):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        result = "You are underweight."
    elif 18.5 <= bmi < 24.9:
        result = "You have a normal weight."
    elif 25 <= bmi < 29.9:
        result = "You are overweight."
    elif bmi >= 30:
        result = "You are obese."
    
    return f"BMI: {bmi:.2f} - {result}"

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("500x500")
window.configure(bg='black')

title_label = tk.Label(window, text="BMI-CALCULATOR", bg='black', fg='white', font='calibri 20 bold')
title_label.pack()

input_frame = tk.Frame(window, bg='black')
input_frame.pack(pady=15)

# Height Label and Entry
height_label = tk.Label(input_frame, text="Enter your height (cm):", bg='black', fg='white', font='calibri 12')
height_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_input = tk.StringVar()
entry = tk.Entry(input_frame, width=30, textvariable=entry_input)
entry.grid(row=0, column=1, padx=10, pady=5)

# Weight Label and Entry
weight_label = tk.Label(input_frame, text="Enter your weight (kg):", bg='black', fg='white', font='calibri 12')
weight_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry2_input = tk.StringVar()
entry2 = tk.Entry(input_frame, width=30, textvariable=entry2_input)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Calculate Button (Centered)
button = tk.Button(input_frame, text="CALCULATE", bg='black', fg='white', font='calibri 10 bold', command=calculate)
button.grid(row=2, column=0, columnspan=2, pady=15)

output_input = tk.StringVar()
output_label = tk.Label(window, text="OUTPUT", bg='black', fg='white', font='calibri 13 bold', textvariable=output_input)
output_label.pack()

window.mainloop()
