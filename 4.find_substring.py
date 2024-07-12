def sub_string(word,str):
   
    if str in word:
        print(f"'{str}' is present in the string '{word}'")
    else:
        print(f"'{str}' is not found")
 
 
word = input("enter the word:")
str = input("enter the substring to be searched:")
sub_string(word,str)
