def match(str1,str2):
    result = ""
    for i in range(min(len(str1),len(str2))):
        result += str1[i]+str2[i]
    return result

str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")
x = match(str1,str2)
print(f"final string is : {x}")