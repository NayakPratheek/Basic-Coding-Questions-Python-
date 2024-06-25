def product_of_num(n):
    prod = 1
    for i in range(1,n+1):
        prod*=i
    return prod
    
n = int(input("enter the number:"))
res = product_of_num(n)
print(f"product of {n} is {res}")