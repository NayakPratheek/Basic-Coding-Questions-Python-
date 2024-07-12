def bubble(arr):
    arr = []
    n = int(input("Enter the number of elements to be added: "))
  
    for i in range(n):
        ele = int(input(f"Enter element {i + 1}: ")) 
        arr.append(ele)
    
    print("Before sorting: ", arr)

    for k in range(n):
        for j in range(k + 1, n):
            if arr[k] > arr[j]:
                t = arr[k]
                arr[k] = arr[j]
                arr[j] = t
    
    print("After sorting: ", arr)


bubble([])
