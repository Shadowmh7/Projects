def get():

  for i in range(100):
    if i % 3==0 and i % 5==0:
      print("FizzBuzz")
    elif i % 5 == 0:
      print(f"Buzz")
    elif i % 3 == 0:
      print("Fizz")
    else :
      print(f"{i} is not in the FizzBuzz category.")

def main():

 get()

if __name__ == "__main__":
    main()
