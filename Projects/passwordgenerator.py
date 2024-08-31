import random
import string 
def generate_password(length):
  letters = string.ascii_letters   
  digits = string.digits           
  symbols = string.punctuation 
  all_characters = letters + digits + symbols


  password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]


  password += random.choices(all_characters, k=length-3)

 
  random.shuffle(password)

   
  return ''.join(password)
name=input("Enter you name id:")
while True:
 print("Generated Password:", generate_password(12))
 while True:
   again=input("You wanna generate a password again :")
   if again in ["yes","no"]:
     break
 if again!="yes":
   print("Exiting")
   break