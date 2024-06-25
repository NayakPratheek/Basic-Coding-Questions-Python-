arr = []

n = int(input("enter the number of elements to be added: "))
for i in range(n):
    ele = input("")
    arr.append(ele)
    arr.sort()

print(f"sorted array is '{arr}'")

for i in range(0,n+1):
    new_arr = arr[::-1]

print(f"descending order array is : {new_arr}")

new = max(arr)
print(new)