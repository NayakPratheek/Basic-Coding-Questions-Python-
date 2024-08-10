def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter how many numbers you want in the series: "))
fibonacci(num)
