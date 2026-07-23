columns = int(input("Enter number columns: "))

for i in range(1,101):
        print(i,end=" ")
        if i % columns == 0 :
            print()