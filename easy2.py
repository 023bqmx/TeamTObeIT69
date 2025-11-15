
def check_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found = []

    for char in text:
        if char in vowels:
            found_vowels.append(char)

    return found_vowels

x = input()
vowels_found = check_vowels(x)
print(vowels_found)