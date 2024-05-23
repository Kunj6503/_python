def pattern(row):
    for i in range(1,row+1):
        for j in range(row-i):
            print(' ', end=' ')
        for k in range(2*i-1):
            print("*", end=' ')
        print()

num_rows = int(input("Enter the number of rows : "))
pattern(num_rows)
