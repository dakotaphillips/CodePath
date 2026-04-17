# ==============================
# Problem Set Version 1 (No Conflicts)
# ==============================


# Problem 1: Cast Vote
# Write a function cast_vote() that records a vote for a candidate.
# If the candidate doesn't exist, add them to the dictionary.

def cast_vote(votes_p1, candidate_p1):
    pass


votes_p1 = {"Alice": 5, "Bob": 3}
cast_vote(votes_p1, "Alice")
print(votes_p1)

cast_vote(votes_p1, "Gina")
print(votes_p1)


# ==============================


# Problem 2: Keys in Common
# Return a list of keys common to both dictionaries.

def common_keys(dict1_p2, dict2_p2):
    pass


dict1_p2 = {"a": 1, "b": 2, "c": 3}
dict2_p2 = {"b": 4, "c": 5, "d": 6}

common_list_p2 = common_keys(dict1_p2, dict2_p2)
print(common_list_p2)


# ==============================


# Problem 3: Frequency Count
# Count occurrences of each integer in a list.

def count_occurrences(nums_p3):
    pass


nums_p3 = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums_p3))


# ==============================


# Problem 4: Highest Priority Task
# Remove and return the task with highest priority.
# If tie, return alphabetically first.

def get_highest_priority_task(tasks_p4):
    pass


tasks_p4 = {
    "task1": 8,
    "task2": 10,
    "task3": 9,
    "task4": 10,
    "task5": 7
}

perform_task1_p4 = get_highest_priority_task(tasks_p4)
print(perform_task1_p4)

perform_task2_p4 = get_highest_priority_task(tasks_p4)
print(perform_task2_p4)

perform_task3_p4 = get_highest_priority_task(tasks_p4)
print(perform_task3_p4)

print(tasks_p4)


# ==============================


# Problem 5: Find Majority Element
# Return element appearing more than n/2 times, else None.

def find_majority_element(elements_p5):
    pass


elements_p5 = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements_p5))


# ==============================


# Problem 6: Has Duplicates
# Return True if duplicates exist within k distance.

def has_duplicates(nums_p6, k_p6):
    pass


nums_p6 = [5, 6, 8, 2, 6, 4, 9]

check1_p6 = has_duplicates(nums_p6, 2)
print(check1_p6)

check2_p6 = has_duplicates(nums_p6, 5)
print(check2_p6)

check3_p6 = has_duplicates(nums_p6, 3)
print(check3_p6)


# ==============================


# Problem 7: Make Pairs
# Return True if list can be divided into equal pairs.

def divide_list(nums_p7):
    pass


nums1_p7 = [3, 2, 3, 2, 2, 2]
print(divide_list(nums1_p7))

nums2_p7 = [1, 2, 3, 4]
print(divide_list(nums2_p7))