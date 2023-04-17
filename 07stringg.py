line = input("Enter a line of text: ")
num_upper = 0
num_lower = 0
num_alpha = 0
num_digits = 0
for ch in line:
    if ch.isupper():
        num_upper += 1
    elif ch.islower():
        num_lower += 1
    elif ch.isalpha():
        num_alpha += 1
    elif ch.isdigit():
        num_digits += 1
print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)
print("Number of alphabets:", num_alpha)
print("Number of digits:", num_digits)
