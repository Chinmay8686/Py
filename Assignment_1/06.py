# Remove Duplicate Elements: Write a program to accept N integers into an array and create a new array containing only the unique elements, removing all duplicate values.

# Accept number of elements
n = int(input("Enter the number of elements: "))

# Accept N integers into an array
arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Create a new array with unique elements in original order
unique_arr = []
seen = set()

for value in arr:
    if value not in seen:
        seen.add(value)
        unique_arr.append(value)

print("Original array:", arr)
print("Unique array:", unique_arr)
