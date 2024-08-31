fruits=["appel","orange","banana","grape"]

items=[]

print("---Welcome to the shoppingcart-----")
while True:
 choose=input(f"please choose an item from the list {fruits} :")
 if choose in fruits:
  quantity=int(input(f"Enter the quantity of the item {choose} :"))
  price=float(input(f"Enter the price of the item {choose} :"))
  store={"Choose":choose,"Quantity":quantity,"Price":price}
  items.append(store)

  more = input("Do you want to add another item? (yes/no): ")
  if more.lower() != "yes":
            break
 else:
  print("Enter an item that exist in the fruit list. ")

print("\n--- Shopping Cart ---")
for store in items:
 print(f"you choosed {store['Choose']}\n the quantity:{store['Quantity']} \n the price :{store['Price']} ")

