import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x600")

# Set the background color to black
root.configure(bg='black')


# Create a label with white text
label = tk.Label(root, text="SHADOW-CHATBOT", bg='black', fg='white',font='calibri 20 bold')
label.pack(padx=20, pady=20)

root_frame=tk.Frame(root,bg='black')
root_frame.pack()

# Create a text area to display the conversation
chat_area = scrolledtext.ScrolledText(root_frame, bg='black', fg='white', wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.pack(pady=10)

# Create an Entry widget for the user to type messages with black background and white text
user_input = tk.Entry(root_frame, bg='black', fg='white', insertbackground='white',width=50)
user_input.pack(pady=10,side="left",padx=25)

# Create a function to handle sending messages
def send_message():
    user_msg = user_input.get()
    display_message(f"You: {user_msg}")
    bot_response = get_response(user_msg)
    display_message(f"Bot: {bot_response}")
    user_input.delete(0, tk.END)

# Display the message in the chat area
def display_message(message):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, message + "\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

# Create a send button
send_button = tk.Button(root_frame,bg='black',fg='white', text="Send",font='calibri 9 bold' ,height=1,width=5,command=send_message)
send_button.pack(side="left")


def simple_response():
 responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm doing well! How about you?",
    "what's the weather like": "I'm not sure, but you can check your local weather app for the latest update!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Anything else I can help with?"
 }
 return responses
def math_response():
 simple_math = {
    "what is 2 + 2": "2 + 2 equals 4.",
    "what is 10 minus 4": "10 minus 4 equals 6.",
    "multiply 3 by 3": "3 times 3 equals 9.",
    "what is 7 divided by 2": "7 divided by 2 equals 3.5."
}
 return simple_math
 
def jokes_response():
 jokes = {
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "another joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "make me laugh": "What do you call fake spaghetti? An impasta!",
    "one more joke": "Why don't oysters share their pearls? Because they are shellfish!"
}
 return jokes
def weather_response():
 weather = {
    "what's the weather like": "I can't check the weather right now, but you can use a weather app!",
    "is it raining": "I'm not sure, but you can check outside or use a weather app.",
    "will it snow today": "I don't have live weather data, but you can check your local weather report!",
    "how's the weather tomorrow": "Check your weather app for the most accurate forecast."
}
 return weather
def culture_response():
 general_culture = {
    "who wrote hamlet": "Hamlet was written by William Shakespeare.",
    "capital of france": "The capital of France is Paris.",
    "largest planet": "The largest planet in our solar system is Jupiter.",
    "how many continents": "There are seven continents on Earth."
}
 return general_culture
def get_response(user):
 user=user.lower()
 if user in simple_response():
  return simple_response()[user]
 elif user in math_response():
  return math_response()[user]
 elif user in weather_response():
  return weather_response()[user]
 elif user in culture_response():
  return culture_response()[user]
 else :
  print("chatbot: I'm not sure I understand. Can you ask that differently?")
root.mainloop()
