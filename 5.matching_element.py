lis = []

n = int(input("enter the number of elements to be insterted : \n"))
for i in range(0,n):
    ele = input("")
    lis.append(ele)

for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i] == lis[j]:
            print(f"Matching element is {lis[i]}")