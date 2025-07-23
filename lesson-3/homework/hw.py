

# Home Work 3 

#task 1

fruits = ["apple", "banana", "cherry", "mango", "grape"]

# Access and print the third fruit (index 2, since indexing starts at 0)
print("The third fruit is:", fruits[2])

#task 2

# Create two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate the two lists
combined_list = list1 + list2

# Print the result
print("Concatenated List:", combined_list)


#task 3 

# Original list of numbers
numbers = [7, 10, 15, 18, 25, 29, 35]

# Get first, middle, and last elements
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

# Store them in a new list
extracted = [first, middle, last]

# Print the result
print("Extracted elements:", extracted)

# task 4

# List of favorite movies
favorite_movies = ["GOL", "The Matrix", "Money", "The Dark Knight", "Gladiator"]

# Convert the list to a tuple
movies_tuple = tuple(favorite_movies)

# Print the result
print("Movies Tuple:", movies_tuple)

# task 5

# List of cities
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]

# Check if "Paris" is in the list
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

# task 6

# Original list
numbers = [1, 2, 3, 4, 5]

# Duplicate using concatenation
duplicated = numbers + numbers

print("Duplicated List:", duplicated)

# task 7 

# Create a tuple of numbers from 1 to 10
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice from index 3 to 7 (elements at index 3, 4, 5, 6)
sliced = numbers[3:7]

# Print the sliced tuple
print("Sliced Tuple:", sliced)

# task 9

# List of colors
colors = ["red", "blue", "green", "blue", "yellow", "blue", "black"]

# Count occurrences of "blue"
blue_count = colors.count("blue")

# Print the result
print("Number of times 'blue' appears:", blue_count)


# task 10

# Tuple of animals
animals = ("dog", "cat", "lion", "tiger", "elephant")

# Find the index of "lion"
lion_index = animals.index("lion")

# Print the result
print("Index of 'lion':", lion_index)


# task 11

# Two tuples of numbers
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Merge the tuples
merged_tuple = tuple1 + tuple2

# Print the result
print("Merged Tuple:", merged_tuple)


# task 12


# task 13

# Tuple of five numbers
numbers_tuple = (10, 20, 30, 40, 50)

# Convert the tuple to a list
numbers_list = list(numbers_tuple)

# Print the result
print("Converted List:", numbers_list)


# task 14

# Tuple of numbers
numbers = (15, 22, 8, 37, 4, 19)

# Find max and min
max_value = max(numbers)
min_value = min(numbers)

# Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)


# task 15

# Tuple of words
words = ("hello", "world", "python", "is", "awesome")

# Reverse the tuple
reversed_words = words[::-1]

# Print the reversed tuple
print("Reversed Tuple:", reversed_words)
