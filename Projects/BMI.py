import tkinter as tk



name=input("Enter your name :")
while True:
 height=int(input(f"Enter your height in cm mr {name} :"))
 weight=int(input(f"Enter your weight in kg mr {name} :"))
 height_m = height / 100
 bmi=weight/(height_m**2)
 if bmi<18.5:
  print(f"mr {name} you are underweight .")
 elif bmi>18.5 and bmi<24.9:
  print(f"mr {name} you have a normal weight .")
 elif bmi>25 and bmi<29.9:
  print(f"mr {name} you are overweight .")
 elif bmi>=30:
  print(f"mr {name} you are fat as fuck .")
 while True:
   again=input("you wanna check your bmi again :")
   if again in ["yes","no"]:
     break
 if again!="yes":
    print("Exiting...")
    break