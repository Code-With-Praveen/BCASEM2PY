string = input("Enter a string: ")
new_string = ""

for i, char in enumerate(string):
    if i % 2 == 0:
        new_string += char.upper()
    else:
        new_string += char.lower()

print("Original string: ", string)
print("Modified string: ", new_string)
