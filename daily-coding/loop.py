num_rows = int(input("Anzahl der Reihen eingeben: "))

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()  

