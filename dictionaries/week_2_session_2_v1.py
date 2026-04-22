# Problem 1: Cast Vote
# Write a function cast_vote() that records a vote for a candidate in an election. 
# The function accepts a dictionary votes that maps candidates to their current number 
# of votes and a string candidate that represents the candidate the user would like to
# vote for. If the candidate doesn't exist, add them to the dictionary. The function 
# should return the updated dictionary.

def cast_vote(votes, candidate):
    pass

# Example Input:
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
# Expected Output:
# {'Alice': 6, 'Bob': 3}

cast_vote(votes, "Gina")
print(votes)
# Expected Output:
# {'Alice': 6, 'Bob': 3, 'Gina': 1}


# Problem 2: Keys in Common
# Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common 
# to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
    pass

# Example Input:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
# Expected Output:
# ['b', 'c']


# Problem 3: Frequency Count
# Write a function that takes in a list of integers nums and counts the number of 
# occurrences of each integer. The function returns the result as a dictionary with 
# integers as keys and their counts as values.

def count_occurrences(nums):
    pass

# Example Input:
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))
# Expected Output:
# {1: 1, 2: 2, 3: 3, 4: 1}


# Problem 4: Highest Priority Task
# Given a dictionary tasks where keys are task names and values are priorities 
# (1-10, where 10 is the highest priority), write a function get_highest_priority_task() 
# that removes the task with the highest priority from the dictionary and returns its name.

def get_highest_priority_task(tasks):
    pass

# Example Input:
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}

perform_task = get_highest_priority_task(tasks)
print(perform_task)
# Expected Output:
# task2

perform_task = get_highest_priority_task(tasks)
print(perform_task)
# Expected Output:
# task4

perform_task = get_highest_priority_task(tasks)
print(perform_task)
# Expected Output:
# task3

print(tasks)
# Expected Output:
# {'task1': 8, 'task5': 7}


# Problem 5: Find Majority Element
# Write a function find_majority_element() that takes in a list of integers elements and 
# finds the majority element in the list.

def find_majority_element(elements):
    pass

# Example Input:
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
# Expected Output:
# 2


# Problem 6: Has Duplicates
# Write a function has_duplicates() that takes in a list of integers nums and a positive 
# number k as parameters.

def has_duplicates(nums, k):
    pass

# Example Input:
nums = [5, 6, 8, 2, 6, 4, 9]

check1 = has_duplicates(nums, 2)
print(check1)
# Expected Output:
# False

check2 = has_duplicates(nums, 5)
print(check2)
# Expected Output:
# True

check3 = has_duplicates(nums, 3)
print(check3)
# Expected Output:
# True


# Problem 7: Make Pairs
# Write a function divide_list() that takes in an integer list nums consisting of 2*n integers as parameters.

def divide_list(nums):
    pass

# Example Input:
nums = [3,2,3,2,2,2]
print(divide_list(nums))
# Expected Output:
# True

nums = [1,2,3,4]
print(divide_list(nums))
# Expected Output:
# False