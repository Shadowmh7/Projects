name=input("Enter the game name : ")
gamesize=float(input(f"Enter the size of {name} :"))
internetspd=float(input(f"Enter your internet speed in (mb/s) :"))
time=gamesize*1024/internetspd
hour=time // 3600
minute=time % 3600 // 60
second=time % 60
if hour==0 and minute==0:
   print(f"{name} gonna be ready in {second:.0f}S")
elif hour==0 and second==0:
   print(f"{name} gonna be ready in {minute:.0f}M")
elif second==0 and minute==0:
   print(f"{name} gonna be ready in {hour:.0f}H")
elif hour==0 and second!=0 and minute!=0:
   print(f"{name} gonna be ready in {minute:.0f}M {second:.0f}S")
elif hour!=0 and second==0 and minute!=0:
   print(f"{name} gonna be ready in {hour:.0f}M {minute:.0f}S")
elif hour!=0 and second!=0 and minute!=0:
   print(f"{name} gonna be ready in {hour:.0f}H {minute:.0f}M {second:.0f}S")