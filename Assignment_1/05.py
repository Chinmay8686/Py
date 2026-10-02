# Reverse the Array: Write a program to accept N integers into an array and display the elements in reverse order without changing the original array.

# Accept number of elements
n = int(input("Enter the number of elements: "))

# Accept N integers into a list
arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Keep the original array unchanged
reversed_arr = arr[::-1]

# Display the result
print("Original array:", arr)
print("Reversed array:", reversed_arr)
