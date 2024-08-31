def print_menu():
    print("----- Inventory Management System Menu -----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Inventory")
    print("5. Exit")
    print("--------------------------------------------")
def add_item(inventory):
    while True:
      name=input("Enter the name of the item :")
      quantity=int(input(f"Enter the quantity of {name} :"))
      price=float(input(f"Enter the price of {name} :"))
      item={"Name":name,"Quantity":quantity,"Price":price}
      inventory.append(item)
      add=input("You wanna add another item (yes/no) :")
      if add.lower()!="yes":
        break

def remove_item(inventory):
     while True:
      choose=input("Enter the name of the item you wanna remove :")
      item_found=False
      for item in inventory:
          if item['Name']==choose:
             item_found=True
             inventory.remove(item)
      print(f"the item {item['Name']} has been removed")

      if not item_found:
        print(f"the item {choose} doesn't exist .")

      again = input("Do you want to remove another item? (yes/no): ")
      if again.lower() != "yes":
            break

def update_item(inventory):
       while True:
        choose = input("Enter the name of the item you want to update: ")
        item_found = False
        for item in inventory:
            if item['Name'] == choose:
                item_found = True
                new_quantity = int(input("Enter the new quantity: "))
                new_price = float(input("Enter the new price: "))
                
                # Update the item details
                item['Quantity'] = new_quantity
                item['Price'] = new_price
                
                print(f"The item '{item['Name']}' has been updated.")
                print(f"Quantity: {item['Quantity']}")
                print(f"Price: {item['Price']}")
                break
        
        if not item_found:
            print(f"The item '{choose}' doesn't exist.")
        
        # Option to exit or continue updating
        again = input("Do you want to update another item? (yes/no): ")
        if again.lower() != "yes":
            break

def print_item(inventory):
   for item in inventory:
       print(f"item :{item['Name']} \nquantiy :{item['Quantity']}\nPrice:{item['Price']}")


def main():
    inventory = []  # This will hold our inventory items

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_item(inventory)

        elif choice == "2":
            remove_item(inventory)

        elif choice == "3":
            update_item(inventory)

        elif choice == "4":
           print_item(inventory)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
