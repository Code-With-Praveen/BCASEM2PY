string = input("Enter a string: ")
consonants = "bcdfghjklmnpqrstvwxyz"
longest_substring = ""
current_substring = ""
for char in string.lower():
    if char in consonants:
        current_substring += char
    else:
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        current_substring = ""
if len(current_substring) > len(longest_substring):
    longest_substring = current_substring
print("The longest substring with only consonants is: ", longest_substring)
