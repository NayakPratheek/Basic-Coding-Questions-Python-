def sum_of_arr(arr):

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
    

n = int(input("enter the number of elements to be added: "))
arr = []

for i in range(n):
    ele = int(input())
    arr.append(ele)

res = sum_of_arr(arr)
print(f"sum of the array is : {res}")