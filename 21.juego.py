arr = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    ele = input("Enter the array element: ")
    arr.append(ele)

visited = set()

for i in range(len(arr)):
    if arr[i] not in visited:
        count = arr.count(arr[i])
        print(f"{count**2}.{arr[i]}", end=" , ")
        visited.add(arr[i])
