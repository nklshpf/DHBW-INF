num_rows = int(input("Enter the number of rows: "))

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()  # Move to the next line after printing each row 

