def factorial(n):
    if n == 0:
        print("factorila of 0 is 0")
    elif n ==1:
        print("factorial of 1 is 1")
    else:
        resu =1
        for i in range(1,n+1):
            resu*=i
        return resu

n = int(input("enter the number:"))
res = factorial(n)
print(f"factorial of {n} is {res}")