n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
while count < n:
    print(f"{a}\r")
    next_term = a + b
    a = b
    b = next_term
    count += 1