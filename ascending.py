arr = []

n = int(input("enter the number of elements to be added: "))
for i in range(n):
    ele = input("")
    arr.append(ele)
    arr.sort()

print(f"ascending order array is '{arr}'")