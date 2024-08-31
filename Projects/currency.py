currency=input("Enter your current currency (mad,dollar,euro,pound):")
while True:
  print("Welcome To the currency service .")
  print("-->1 convert to dollar.")
  print("-->2 convert to euro.")
  print("-->3 convert to pound.")
  print("-->4 convert to mad.")
  while True:
   choose=input("choose the curency you wanna convert to :")
   if choose in ["dollar","euro","pound","mad"]:
     break
   else :
     print("Enter a valid option.")
  if choose=="dollar":
    if currency=="mad":
      mad=float(input("Enter your money :"))
      total=mad/10.32
      print(f"{total:.2f}dollar is equale to {mad}mad")
    if currency=="dollar":
      print(f"you can't convert to the same currency")
    if currency=="euro":
      euro=float(input("Enter your money :"))
      total=euro/1.10
      print(f"{total:.2f}dollar is equale to {euro}euro")
    if currency=="pound":
      pound=float(input("Enter your money :"))
      total=pound/1.27
      print(f"{total:.2f}dollar is equale to {pound}pound")

  if choose=="euro":
    if currency=="mad":
      mad=float(input("Enter your money :"))
      total=mad/10.73
      print(f"{total:.2f}euro is equale to {mad}mad")
    if currency=="dollar":
      dollar=float(input("Enter your money :"))
      total=dollar*1.10
      print(f"{total:.2f}euro is equale to {dollar}dollar")
    if currency=="euro":
      print(f"you can't convert to the same currency")
    if currency=="pound":
      pound=float(input("Enter your money :"))
      total=pound*1.16
      print(f"{total:.2f}euro is equale to {pound}pound")

  if choose=="pound":
    if currency=="mad":
      mad=float(input("Enter your money :"))
      total=mad/12.56
      print(f"{total:.2f}pound is equale to {mad}mad")
    if currency=="dollar":
      dollar=float(input("Enter your money :"))
      total=dollar*1.27
      print(f"{total:.2f}pound is equale to {dollar}dollar")
    if currency=="euro":
      euro=float(input("Enter your money :"))
      total=euro*1.17
      print(f"{total:.2f}pound is equale to {euro}euro")
    if currency=="pound":
        print(f"you can't convert to the same currency")

  if choose=="mad":
    if currency=="mad":
      print(f"you can't convert to the same currency")
    if currency=="dollar":
      dollar=float(input("Enter your money :"))
      total=dollar*10.32
      print(f"{total:.2f}mad is equale to {dollar}dollar")
    if currency=="euro":
      euro=float(input("Enter your money :"))
      total=euro*10.73
      print(f"{total:.2f}mad is equale to {euro}euro")
    if currency=="pound":
      pound=float(input("Enter your money :"))
      total=pound*12.56
      print(f"{total:.2f}mad is equale to {pound}pound")
  while True:
   again=input("you wanna go back to the menu :")
   if again in ["yes","no"]:
     break
  if again!="yes":
    print("Exiting...")
    break