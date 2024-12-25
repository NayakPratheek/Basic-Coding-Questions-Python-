str1 = input("enter the string:")
str2 = str1.split()
str3 = []

for i in range(len(str2)):
    str3.append(str2[i][::-1])

result = " ".join(str3)
print(result)
