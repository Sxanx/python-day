rows = int(input("Enter number row: "))
columns = int(input("Enter number columns: "))

for i in range(rows):
    for j in range(columns):
        print('*',end="")
    print()