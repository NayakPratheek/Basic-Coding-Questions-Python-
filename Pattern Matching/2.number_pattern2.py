# To print the pattern of 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input("enter the number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()