# To print the following star pattern (Pyramid pattern):

#    *               *
#   ***             ***
#  *****           *****
#                 *******

n = int(input("enter the number of rows : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()