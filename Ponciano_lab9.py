rows_of_number = int(input("Enter the number of rows: "))

num = 1
for row in range(1, rows_of_number + 1):
    for column in range(row):
        print(num, end=" ")
        num = num + 1
    print()
