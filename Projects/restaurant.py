def print_menu():
    print("----- Restaurant Menu -----")
    print("1. Add a new order")
    print("2. View all orders")
    print("3. Calculate total")
    print("4. Exit")
    print("---------------------------")


def add_orders(order,menu):
  while True:
    meal=input(f"Choose an order from the {menu} :")
    if meal in menu:
      quantity=int(input(f"Enter the quantity of the {meal} :"))
      total=menu[meal]*quantity
      info={"Meal":meal,"Quantity":quantity,"Total":total}
      order.append(info)
      add=input("You wanna add an other order (yes/no):")
      if add.lower()!="yes":
         break
    else:
      print("Choose an order that exist in the menu.")


def main():
  order = []
  menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Salad": 4.99,
    "Pasta": 7.99,
    "Soda": 1.99,
    "Coffee": 2.49
 }
  print("---Welcome To The Restaurant Menu---")
  while True:
   print_menu()
   choose=input("Choose an option :")

   if choose=="1":
    add_orders(order,menu)

   elif choose=="2":
      for info in order:
       print(f"order :{info['Meal']} \nQuantity:{info['Quantity']}\n Total:{info['Total']}")
       print("__________________________")
   elif choose=="3":
     total=0
     for info in order:
      total+=info['Total']
     print(f"Summary:{total}")
       

   elif choose=="4":
     print("Exiting...")
     break

     
if __name__=="__main__":
   main()


