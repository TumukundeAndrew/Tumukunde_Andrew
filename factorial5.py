def factorial(n):
    
    # factorial of 0 and 1 ia always 1, so the function returns 1 immwdiately in these cases
    if n == 0 or n == 1:
        return 1
    #multiply n by the factoral of the number just before it (n-1)
    return n * factorial(n - 1)

# Find the factorial of 5
result = factorial(5)
print("Factorial of 5 is:", result)
