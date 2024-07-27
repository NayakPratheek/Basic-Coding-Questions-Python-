def prime(n):
   

    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n**0.5+1):
        if n%i==0:
            return False
    return True
n = int(input("enter the number:"))
prime(n)

or

def prime(n):
    if n <= 1:
        return False  # 0, 1, and negative numbers are not prime
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime

    # Check only odd numbers from 3 up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):#here 2 refers to the step size,checking only odd numbers
        if n % i == 0:
            return False
    return True


n = int(input("Enter the number: "))
if prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
