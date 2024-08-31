def convo():
  convo={
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm doing well! How about you?",
    "what's the weather like": "I'm not sure, but you can check your local weather app for the latest update!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Anything else I can help with?"
  }
  return convo

def get(user):
  if user in convo():
    return convo()[user]
  else:
    print("chatbot : I'm not sure I understand. Can you ask that differently?")

def main():
 while True:
  user=input("you:").lower().strip()
  response=get(user)
  if user in ["bye"]:
   print(response)
   break
  else:
    print(response)

if __name__=="__main__":
  main()