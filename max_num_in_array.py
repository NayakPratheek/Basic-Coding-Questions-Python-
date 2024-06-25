arr = []

n = int(input("enter the number of elements to be added: "))
for i in range(n):
    ele = input("")
    arr.append(ele)

print(f"maximum number in the array is {max(arr)}")