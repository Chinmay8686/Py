#
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        # Print 1 if row + col sum is even, else print 0
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()