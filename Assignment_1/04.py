n = int(input("Enter the number of elements: "))
numbers = []

for index in range(n):
	numbers.append(int(input(f"Enter element {index + 1}: ")))

target = int(input("Enter the number to search: "))

for index, number in enumerate(numbers):
	if number == target:
		print(f"{target} is present at position {index + 1}.")
		break
else:
	print(f"{target} is not present in the array.")