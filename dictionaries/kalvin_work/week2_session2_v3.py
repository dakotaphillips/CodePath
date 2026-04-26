# Problem 1: Return Book
# Write a function return_book() that accepts a string title and a dictionary library as parameters. 
# library maps book titles to the number of copies the library currently has in stock. 
# The function should increment the quantity of the book title in library by 1. 
# If title is not in the library, then add it and set quantity to 1. Return the updated library dictionary.

def return_book(title, library):
    pass

# Example Input:
library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)
# Expected Output:
# {'The Hobbit': 2, '1984': 2, 'The Great Gatsby': 4}

updated_lib = return_book("The Giver", library)
print(updated_lib)
# Expected Output:
# {'The Hobbit': 2, '1984': 1, 'The Great Gatsby': 4, 'The Giver': 1}


# Problem 2: Dictionary Difference
# Write a function dict_difference() that takes two dictionaries and returns a new dictionary 
# that contains only the key-value pairs found only in the first dictionary but not in the second.

def dict_difference(d1, d2):
    pass

# Example Input:
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))
# Expected Output:
# {'a': 1, 'c': 3, 'd': 4}


# Problem 3: Take from Stock
# Write a function pop_stock() that takes a dictionary of items items that keeps track of an 
# item and its stock quantity, an item_name, and a quantity to be removed as parameters.

def pop_stock(items, item_name, quantity):
    pass

# Example Input:
items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
# Expected Output:
# {'chocolate': 20, 'candy': 3, 'chips': 10}

print(resultB)
# Expected Output:
# Not enough stock

print(resultC)
# Expected Output:
# Item does not exist

print(resultD)
# Expected Output:
# {'chocolate': 15, 'candy': 3, 'chips': 10}


# Problem 4: Group By Frequency
# Write a function group_by_frequency() that takes in a list lst and returns a dictionary 
# where keys represent the frequency of unique elements within lst and values represent a 
# list of elements with the same frequency.

def group_by_frequency(lst):
    pass

# Example Input:
lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
# Expected Output:
# {1: ['a', 'b'], 2: ['c', 'd'], 3: ['e']}


# Problem 5: No Duplicates Allowed
# Write a function that takes in a list of integers nums as a parameter and removes all duplicates. 
# The function should return a list containing the unique elements in the order of their 
# last occurrence in the original list.

def remove_duplicates_from_front(nums):
    pass

# Example Input:
nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))
# Expected Output:
# [6, 5, 2, 8, 3]


# Problem 6: First Repeating Element
# Write a function find_min_index_of_repeating() that takes in an integer list nums as a 
# parameter and returns the minimum index of an element that has a duplicate value.

def find_min_index_of_repeating(nums):
    pass

# Example Input:
nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [5, 6, 2, 4, 3, 4, 3]

print(find_min_index_of_repeating(nums))
# Expected Output:
# 1

print(find_min_index_of_repeating(nums2))
# Expected Output:
# None

print(find_min_index_of_repeating(nums3))
# Expected Output:
# 3


# Problem 7: Target Sum
# Write a function two_sum() that takes in a list of integers nums and an integer target as parameters.

def two_sum(nums, target):
    pass

# Example Input:
nums = [2,7,11,15]
q_1 = two_sum(nums, 9)
q_2 = two_sum(nums, 18)

nums2 = [3,3]
q_3 = two_sum(nums2, 6)

print(q_1)
# Expected Output:
# [0, 1]

print(q_2)
# Expected Output:
# [1, 2]

print(q_3)
# Expected Output:
# [0, 1]