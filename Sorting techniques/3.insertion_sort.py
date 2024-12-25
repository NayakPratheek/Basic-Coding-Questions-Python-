class Sorting:
    def insert(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


n = int(input("Enter the number of elements to be inserted: "))
arr = []
for i in range(n):
    ele = int(input(f"Enter the element {i + 1}: "))
    arr.append(ele)

s = Sorting
sorted_arr = s.insert(arr)
print("Sorted array:", sorted_arr)
