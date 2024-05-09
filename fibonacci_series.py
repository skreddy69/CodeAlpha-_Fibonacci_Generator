def fib(limit):
    # Initialize the first two Fibonacci numbers
    fib = [0, 1]
    
    # Generate Fibonacci numbers until the limit is reached
    while fib[-1] + fib[-2] <= limit:
        # Add the next Fibonacci number to the list
        fib.append(fib[-1] + fib[-2])
    
    return fib

# Example usage
limit = int(input("Enter the limit for the Fibonacci series: "))
fib_series = fib(limit)
print("Fibonacci series up to", limit, ":", fib_series)
