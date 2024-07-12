str = input("enter the string : ")
c=0
v=0

str_inp = str.lower()

vow ="aeiou"

for char in str_inp:
    if char in vow:
        v+=1
    else:
        c+=1

print(f"vowels count is : {v}\n")
print(f"consonant count is : {c}\n")