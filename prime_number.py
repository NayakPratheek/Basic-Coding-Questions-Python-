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