def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example
print(factorial_iterative(5))  # Output: 120
