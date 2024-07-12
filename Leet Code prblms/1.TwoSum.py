arr = [10,20,30,12,102]
tar = int(input(""))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == tar:
            print("")
            print(arr[i],arr[j])  
         