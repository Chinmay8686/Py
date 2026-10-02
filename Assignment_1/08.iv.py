#
rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    print("  " * (rows - i), end="")
    
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
        
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
        
    print()