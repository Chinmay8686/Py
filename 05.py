#output : 
        # 5 4 3 2 1  
        # 4 3 2 1 
        # 3 2 1
        # 2 1 
        # 1
# i -> 5 rows -> 5 to 1 
# j ->  1 to i 
n=5

for i in range (n, 0, -1):
   for j in range(i, 0, -1):
    print(j, end =" ")
   print()
