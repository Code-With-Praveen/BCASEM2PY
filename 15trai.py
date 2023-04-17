inp = int(input("Enter the num of element:"))
for i in range(0,inp+1):
    for j in range(inp, i, -1):
        print(j, end='')
    print()
