def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        input_string = input_string.replace(vowel, "")
    return input_string

# Example usage:
input_str = input("Enter a string: ")
result = remove_vowels(input_str)
print(f"The string without vowels: {result}")
