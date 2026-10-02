# Move Zeros to the End: Write a program to accept N integers into an array and rearrange the elements so that all 0 values are moved to the end while maintaining the relative order of the non-zero elements.

# Accept number of elements
n = int(input("Enter the number of elements: "))

# Accept N integers into an array
arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Keep relative order of non-zero elements and move zeros to the end
result = []
zero_count = 0

for value in arr:
    if value != 0:
        result.append(value)
    else:
        zero_count += 1

result.extend([0] * zero_count)

print("Original array:", arr)
print("Array after moving zeros to the end:", result)
