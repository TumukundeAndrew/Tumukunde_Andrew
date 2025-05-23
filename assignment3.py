def divide_numbers(n, m):
    return n / m  

while True:
    try:
        number1 = int(input("Enter number1: "))
        number2 = int(input("Enter number2: "))
        
        result = divide_numbers(number1, number2)
        
    except ValueError:
        print("Invalid number! Enter a valid integer.")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Enter a non-zero number.")
    else:
        print(f"The result is: {result}")
        break  
