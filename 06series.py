n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n+1):
    if i == 1:
        term = 1
    else:
        term = i / (i * (i - 1))
    if i % 2 == 0:
        sum -= term
    else:
        sum += term
print("The sum of the series for", n, "terms is", sum)
