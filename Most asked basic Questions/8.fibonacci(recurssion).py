def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(fibonacci(i))
    return series

n = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci_series(n))