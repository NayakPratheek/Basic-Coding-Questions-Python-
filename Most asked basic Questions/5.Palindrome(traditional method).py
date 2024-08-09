def isPali(stri):
    new_str = str.lower()
    left, right = 0, len(new_str)-1
    while left<right:
        if new_str[left] != new_str[right]:
            print("Not pali")
            return
        left+=1
        right-=1
    print("Pali")
str = input("enter text : ")
isPali(str)
