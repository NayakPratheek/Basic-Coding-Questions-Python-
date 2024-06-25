def sumofnum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

n = int(input("enter the number till where the numbers are to be added:"))
res = sumofnum(n)
print(f"sum of {n} numbers is {res}")