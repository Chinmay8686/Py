#output : 1
        # 1 2 
        # 1 2 3 
        # 1 2 3 4 
        # 1 2 3 4 5 
# i -> 5 rows -> 1 to 5 
# j ->  1 to i 
n=5

for i in range (1, n+1):
   for j in range(1, i+1):
    print(j, end = "  ")
   print()
