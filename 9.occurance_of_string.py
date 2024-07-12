str = input("enter the text:\n")
target = input("enter the target string : ")
c=0
for i in range(len(str)):
    if str[i] == target:
        c+=1
print(f"{target} occurs {c} times")