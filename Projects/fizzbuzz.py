import tkinter as tk

def get():
     try:
        while True:
            num = int(entry.get())  # Convert the input to an integer
            if 1 <= num <= 100:  # Check if the number is in the valid range
                break  # Exit the loop if the number is valid
            else:
                text.set("Enter a number between 1 and 100")
                return  # Exit the function to avoid re-running the loop
     except ValueError:
        text.set("Please enter a valid number.")
        return
     if num % 5 == 0 and num % 3 == 0:
      text.set("Fizz_Buzz")
     elif num % 3 == 0:
      text.set("Fizz")
     elif num % 5 == 0:
      text.set("Buzz")
     else:
      text.set(f"the number {num} is not in the FizzBuzz categorie")





window=tk.Tk()
window.title("FizzBuzz")
window.geometry("400x500")
window.config(bg='black')

window_label=tk.Label(window,text="Fizz_Buzz",bg='black',fg='white',font='calibri 15 bold')
window_label.pack()

description_label=tk.Label(window,text="Enter a number between 1 and 100",bg='black',fg='white',font='calibri 12 bold')
description_label.pack()

frame_input=tk.Frame(window,bg='black')
frame_input.pack()

entry=tk.IntVar()
entry1=tk.Entry(frame_input,width=20,textvariable=entry)
entry1.pack(pady=10,side='left')

button=tk.Button(frame_input,text='FizzBuzz',fg='white',bg='black',font='calibri 10 bold',command=get)
button.pack(padx=10,pady=10,side='left')

text=tk.StringVar()
text_description=tk.Label(window,text="",bg='black',fg='white',font='calibri 14 bold',textvariable=text)
text_description.pack()


window.mainloop()