import tkinter as tk

def convert():
    currency = entry.get()
    choose = entry1.get()
    
    if choose not in ["dollar", "euro", "pound", "mad"]:
        descri.set("Enter a valid option.")
        return
    
    amount = float(entry2.get())
    
    if currency == choose:
        descri.set("You can't convert to the same currency")
        return
    
    conversion_rates = {
        ("mad", "dollar"): 1/10.32,
        ("mad", "euro"): 1/10.73,
        ("mad", "pound"): 1/12.56,
        ("dollar", "mad"): 10.32,
        ("euro", "mad"): 10.73,
        ("pound", "mad"): 12.56,
        ("dollar", "euro"): 1/1.10,
        ("euro", "dollar"): 1.10,
        ("dollar", "pound"): 1/1.27,
        ("pound", "dollar"): 1.27,
        ("euro", "pound"): 1.16,
        ("pound", "euro"): 1/1.16
    }
    
    total = amount * conversion_rates.get((currency, choose), 0)
    descri.set(f"{amount:.2f} {currency} is equal to {total:.2f} {choose}")

window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x500")
window.configure(bg='black')

# Title Label
window_label = tk.Label(window, text='CURRENCY CONVERTER', bg='black', fg='white', font='calibri 15 bold')
window_label.pack(pady=15)

# Input for Current Currency
descri_label = tk.Label(window, text='Enter your current currency (mad, dollar, euro, pound)', bg='black', fg='white', font='calibri 12 bold')
descri_label.pack()

entry = tk.StringVar()
entry1_entry = tk.Entry(window, textvariable=entry, width=20)
entry1_entry.pack()

# Input for Currency to Convert To
descri1_label = tk.Label(window, text='Choose the currency you want to convert to:', bg='black', fg='white', font='calibri 12 bold')
descri1_label.pack()

entry1 = tk.StringVar()
entry2_entry = tk.Entry(window, textvariable=entry1, width=20)
entry2_entry.pack()

# Input for Amount of Money
descri2_label = tk.Label(window, text='Enter your amount:', bg='black', fg='white', font='calibri 12 bold')
descri2_label.pack()

entry2 = tk.StringVar()
entry3_entry = tk.Entry(window, textvariable=entry2, width=20)
entry3_entry.pack()

# Convert Button
button_label = tk.Button(window, text='CONVERT', fg='white', bg='black', font='calibri 10 bold', command=convert)
button_label.pack(pady=10)

# Output Label
descri = tk.StringVar()
descri3_label = tk.Label(window, textvariable=descri, bg='black', fg='white', font='calibri 12 bold')
descri3_label.pack()

window.mainloop()
