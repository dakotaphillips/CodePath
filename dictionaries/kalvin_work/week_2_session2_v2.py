# Problem 1: Update Score
# Write a function update_score() that takes in a dictionary scores that maps 
# player names to current scores, a string player, and an integer points as parameters. 
# The function adds the points to the current score of player in the dictionary 
# and returns the updated dictionary. If the player does not exist in scores, then add them.

def update_score(scores, players, points):
    pass

# Example Input:
scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
# Expected Output:
# {'Alice': 110, 'Bob': 90}

update_score(scores, "Calvin", 20)
print(scores)
# Expected Output:
# {'Alice': 110, 'Bob': 90, 'Calvin': 20}

update_score(scores, "Calvin", 5)
print(scores)
# Expected Output:
# {'Alice': 110, 'Bob': 90, 'Calvin': 25}


# Problem 2: Dictionary Intersection
# Write a function dict_intersection() that takes in two dictionaries as 
# parameters and returns a new dictionary containing the key-value pairs found in both dictionaries.

def dict_intersection(d1, d2):
    pass

# Example Input:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}

# Expected Output:
# {'b': 2}


# Problem 3: Filter by Price
# Write a function that takes in a dictionary of items and a price_threshold as parameters. 
# The function should iterate through the dictionary and remove all items that has a value 
# less than price_threshold. The function also returns a list of all items that are removed. 
# If no item satisfies the condition, return None.

def remove_items_below_price(items, price_threshold):
    pass

# Example Input:
items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
# Expected Output:
# ["banana", "date"]

removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)
# Expected Output:
# None


# Problem 4: Find Odd Occurrences
# Write a function find_odd_occurrences() that takes in a list of integers numbers where all 
# numbers occur an even number of times except for two unique numbers that occur an odd number of times. 
# The function should find the two unique numbers and return them as a list. 
# Assume each problem has exactly one solution.

def find_odd_occurrences(numbers):
    pass

# Example Input:
numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)
# Expected Output:
# [1, 3]


# Problem 5: Find Mode
# Write a function find_mode() that takes in a non-empty list of integers lst as a parameter. 
# The function returns the mode (the most frequently occurring number) and if there is a tie, 
# return the element which appeared first in the list.

def find_mode(lst):
    pass

# Example Input:
lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)
# Expected Output:
# 4


# Problem 6: How Many Smaller
# Write a function smaller_numbers_than_current() that takes in a list of numbers nums as a parameter. 
# For each nums[i], the function should find out how many numbers in the list are smaller than it.

def smaller_numbers_than_current(nums):
    pass

# Example Input:
nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
# Expected Output:
# [4, 0, 1, 1, 3]


# Problem 7: Good Pairs
# Write a function num_identical_pairs() that takes in a list of integers nums and returns the 
# number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def num_identical_pairs(nums):
    pass

# Example Input:
nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))
# Expected Output:
# 4

nums = [1,2,3]
print(num_identical_pairs(nums))
# Expected Output:
# 0

nums = [1,1,1,1]
print(num_identical_pairs(nums))
# Expected Output:
# 6