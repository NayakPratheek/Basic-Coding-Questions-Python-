def minimum(arr):
     
     print("enter the array elements: ")
     for i in range(n):
          ele = input("")
          arr.append(ele)

     minim = arr[0]
     for i in range(1,len(arr)): 
          if arr[i] < minim:
               minim = arr[i]
     return minim


arr = []               
n = int(input("enter the number of elements to be insterted: "))
min_num = minimum(arr)
print(f"minimum number of the array is {min_num}")