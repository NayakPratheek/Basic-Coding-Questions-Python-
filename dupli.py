str1 = input("Enter the string: ")
str2 = []
for i in str1:
    if i not in str2:
        str2.append(i)
print(''.join(str2))