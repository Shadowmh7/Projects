def print_menu_users():
    print("----- Library Management System Menu -----")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. View available books")
    print("6. Exit")
    print("------------------------------------------")


def add(library):
 while True:
  title=input("Enter the book Title :")
  author=input(f"Enter {title} author :")
  year=input(f"Enter the Year of {title} :")
  status=input("is the book available or unavailable :")
  books={"Title":title,"Author":author,"Year":year,"Status":status}
  library.append(books)
  add=input("You wanna add another book (yes/no) :")
  if add.lower()!="yes":
    break

def users(library):
  while True:
   print_menu_users()
   choose=input("Choose an option :")
   
   if choose=="1":
     add(library)

   elif choose=="2":
      for books in library:
        print(f"Title:{books['Title']} \n Author : {books['Author']} \n Year:{books['Year']} \n Status :{books['Status']}")

   elif choose=="3":
      check=input("Check the book :")
      for books in library:
        if books['Title']==check:
         if books['Status'] == "available":
            books['Status'] = "unavailable"
            print(f"The book '{books['Title']}' has been checked out and is now unavailable.")
        else:
            print(f"The book '{books['Title']}' is already unavailable.")

   elif choose=="4":
      returne=input("Enter the book you wanna return :")
      for books in library:
         if returne==books['Title']:
           if books['Status']=="unavailable":
            books['Status'] = "available"
            print(f"The book '{books['Title']}' has been checked out and is now available.")
         else:
            print(f"The book '{books['Title']}' is already available.")

   elif choose=="5":
     for books in library:
       if books['Status']=="available":
         print(f"Title:{books['Title']} \n Author : {books['Author']} \n Year:{books['Year']} \n Status :{books['Status']}")
   
   elif choose=="6":
     print("Exiting...")
     break

def print_menu_guest():
    print("----- Library Management System Menu -----")
    print("1. View all books")
    print("2. View available books")
    print("3. Exit")
    print("------------------------------------------")

def guest(library):
  while True:
   print_menu_guest()
   choose=input("Choose an option :")
   
   if choose=="1":
      for books in library:
        print(f"Title:{books['Title']} \n Author : {books['Author']} \n Year:{books['Year']} \n Status :{books['Status']}")

   elif choose=="2":
     for books in library:
       if books['Status']=="available":
         print(f"Title:{books['Title']} \n Author : {books['Author']} \n Year:{books['Year']} \n Status :{books['Status']}")
   
   elif choose=="3":
     print("Exiting...")
     break
   

def access():
   print("---Library Log in---")
   name=input("Enter your name :")
   password=input("Create a password :")
   while True:
     check=input("Re-enter your password :")
     if check == password:
       print(f"Welcome {name} ")
       break
     else:
       print("The password is inccorect Try again.")

def main():

 library= [
    {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Year": 1813, "Status": "available"},
    {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year": 1925, "Status": "available"},
    {"Title": "Moby Dick", "Author": "Herman Melville", "Year": 1851, "Status": "available"},
    {"Title": "1984", "Author": "George Orwell", "Year": 1949, "Status": "available"},
    {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year": 1960, "Status": "available"},
    {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Year": 1951, "Status": "available"},
    {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Year": 1937, "Status": "available"},
    {"Title": "War and Peace", "Author": "Leo Tolstoy", "Year": 1869, "Status": "available"},
    {"Title": "The Odyssey", "Author": "Homer", "Year": -800, "Status": "available"},
    {"Title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Year": 1866, "Status": "available"}
  ]
 while True:
   info=input("You wanna enter as user or guest :").lower().strip()
   if info in ["user","guest"]:
    if info=="user":
     access()
     print_menu_users()
     users(library)
     break
    elif info=="guest":
     guest(library)
     break
   else:
    print("Enter a valid ansewer (user/guest).")
  
if __name__=="__main__":
   main()