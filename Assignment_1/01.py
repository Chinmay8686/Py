#calculate Array sum: Write a program to accept N integers into an array and calculate and display the sum of all elements. 
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))
total = sum(arr)
print("The sum of all elements is:", total)