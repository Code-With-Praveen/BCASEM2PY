line = input("Enter a line of text: ")
substring = input("Enter a substring to search for: ")
count = line.count(substring)
print("The substring '{0}' appears {1} times in the line.".format(substring, count))
