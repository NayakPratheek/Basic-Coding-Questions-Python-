# To print the following * pattern :

#     *
#    **
#   ***
#  ****
# *****




n = int(input("enter the number of rows: "))
for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * i, end="")
    print()