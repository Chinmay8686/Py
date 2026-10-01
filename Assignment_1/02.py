# Find the largest, second-largest, smallest, and second-smallest distinct values.

count = int(input("Enter the number of integers: "))
numbers = list(map(int, input(f"Enter {count} integers separated by spaces: ").split()))

if count < 2:
	print("Enter at least two integers.")
elif len(numbers) != count:
	print(f"Expected {count} integers, but received {len(numbers)}.")
else:
	largest = second_largest = None
	smallest = second_smallest = None

	for number in numbers:
		if largest is None or number > largest:
			second_largest = largest
			largest = number
		elif number != largest and (second_largest is None or number > second_largest):
			second_largest = number

		if smallest is None or number < smallest:
			second_smallest = smallest
			smallest = number
		elif number != smallest and (second_smallest is None or number < second_smallest):
			second_smallest = number

	if second_largest is None or second_smallest is None:
		print("At least two distinct integers are required.")
	else:
		print("Largest:", largest)
		print("Second largest:", second_largest)
		print("Smallest:", smallest)
		print("Second smallest:", second_smallest)
