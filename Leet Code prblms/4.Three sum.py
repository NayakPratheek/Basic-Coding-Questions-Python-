def threesum(arr, tar):
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == tar:
                    print(f"Triplet is {[arr[i], arr[j], arr[k]]}")
                    return True
    return False

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    arr.append(ele)

tar = int(input("Enter the target: "))
ts = threesum(arr, tar)
print(ts)
