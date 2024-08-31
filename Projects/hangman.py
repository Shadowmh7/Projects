import random

def rand():
  string=["appel","orange","banana","lemon"]
  generate=random.choice(string)
  return generate


def main(): 
 while True:
  gen=rand()
  num=len(gen)
  i=0
  while i<=3:
   ansewr=input(f"Attempt {i+1}: Guess a fruit that contain {num} :")

   if ansewr==gen:
     print(f"You won the word is {gen}")
     break
   elif ansewr!=gen:
     print("False try again.")
     i+=1
  if i>=3:
   print(f"you lost the ansewr is {gen}")
  while True:
   ansewr=input("you wanna play again :").lower().strip()
   if ansewr in ["yes","no"]:
     break
  if ansewr!="yes":
   print("Exiting...")
   break

if __name__ == "__main__":
    main()