while True:
  try:
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    
    result = number1/number2
    
  except ValueError:
    print("invalid number! enter a valid interger.")
  except ZeroDivisionError:
    print("division by zero is not allowed. enetr a non zero number")
  else:
    print(f"{number1}/{number2} = {result}")
    break                  
        