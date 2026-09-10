# Aim: To perform various operations on Python lists
# and use built-in list functions.

# Create a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("Sliced List:", numbers[1:4])

# Adding elements
numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

# Removing elements
numbers.remove(25)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

# Sorting
numbers.sort(reverse=True)
print("After sorting:", numbers)

# Built-in list functions
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))