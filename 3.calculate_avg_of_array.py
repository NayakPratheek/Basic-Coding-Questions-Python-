def average(arr):
    sum = 0
    avg = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    return avg

n = int(input("Enter the number of elements to be added: "))
arr = []

print("Enter the array elements:")
for i in range(n):
    ele = int(input())
    arr.append(ele)

average_value = average(arr)
print(f"Average of numbers in the array is: {average_value}")
