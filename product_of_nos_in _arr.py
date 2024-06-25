def product(arr):

    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    return prod

arr = []
n = int(input("enter the number of elements to be added: "))

for i in range(n):
    ele = int(input())
    arr.append(ele)

res = product(arr)
print(f"product of numbers of the array is : {res}")