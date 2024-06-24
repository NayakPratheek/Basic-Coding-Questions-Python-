str = input("enter the text\n")

str_rev = str[::-1]

if str_rev == str:
    print(f"{str} is a Palindrome")
else:
    print(f"{str} is not a Palindrome")    