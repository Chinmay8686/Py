# Count Substrings: Find all occurrences of substring in a given string.

text = input("Enter the main string: ")
pattern = input("Enter the substring to find: ")

positions = []
start = 0

while True:
    index = text.find(pattern, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

print("Substring occurrences at positions:", positions)
print("Total occurrences:", len(positions))
