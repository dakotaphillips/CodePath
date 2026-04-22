# ==============================
# Problem Set Version 1 (No Conflicts)
# ==============================


# Problem 1: Cast Vote
# Write a function cast_vote() that records a vote for a candidate.
# If the candidate doesn't exist, add them to the dictionary.

# def cast_vote(votes_p1, candidate_p1):
#     if candidate_p1 in votes_p1:
#         votes_p1[candidate_p1] += 1
#     else:
#         votes_p1[candidate_p1] = 1


# votes_p1 = {"Alice": 5, "Bob": 3}
# cast_vote(votes_p1, "Alice")
# print(votes_p1)

# cast_vote(votes_p1, "Gina")
# print(votes_p1)


# ==============================


# Problem 2: Keys in Common
# Return a list of keys common to both dictionaries.

# def common_keys(dict1_p2, dict2_p2):
#     common_keys = []
#     for key in dict1_p2:
#         if key in dict2_p2:
#             common_keys.append(key)
#     return common_keys


# dict1_p2 = {"a": 1, "b": 2, "c": 3}
# dict2_p2 = {"b": 4, "c": 5, "d": 6}

# common_list_p2 = common_keys(dict1_p2, dict2_p2)
# print(common_list_p2)


# ==============================


# Problem 3: Frequency Count
# Count occurrences of each integer in a list.

# def count_occurrences(nums_p3):
#     freq = {}
#     for num in nums_p3:
#         if num not in freq:
#             freq[num] = 1
#         else:
#             freq[num] += 1
#     return freq


# nums_p3 = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums_p3))


# ==============================


# Problem 4: Highest Priority Task
# Remove and return the task with highest priority.
# If tie, return alphabetically first.

# def get_highest_priority_task(tasks_p4):
#     priority = {}
#     for key, value in tasks_p4.items():
#         if value not in priority:
#             priority[value] = [key]
#         else:
#             priority[value].append(key)
    
#     highest_priority = sorted(priority[max(priority)])
#     del tasks_p4[highest_priority[0]]
#     return highest_priority[0]


# tasks_p4 = {
#     "task1": 8,
#     "task2": 10,
#     "task3": 9,
#     "task4": 10,
#     "task5": 7
# }

# perform_task1_p4 = get_highest_priority_task(tasks_p4)
# print(perform_task1_p4)

# perform_task2_p4 = get_highest_priority_task(tasks_p4)
# print(perform_task2_p4)

# perform_task3_p4 = get_highest_priority_task(tasks_p4)
# print(perform_task3_p4)

# print(tasks_p4)


# ==============================


# Problem 5: Find Majority Element
# Return element appearing more than n/2 times, else None.

# def find_majority_element(elements_p5):
#     freq = {}
#     for num in elements_p5:
#         if num not in freq:
#             freq[num] = 1
#         else:
#             freq[num] += 1
    
#     list_size = len(elements_p5)

#     for key, value in freq.items():
#         if value > list_size/2:
#             return key
    
#     return None


# elements_p5 = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements_p5))


# ==============================


# Problem 6: Has Duplicates
# Write a function has_duplicates() that takes in a list of integers nums and
#  a positive number k as parameters. The function returns True if the list 
# contains any duplicate elements within k (inclusive) indices of each other. 
# In other words, return True if nums[i] has the same value as any of the k 
# neighboring elements to its left or right. If k is greater than the list's length, 
# the solution should check for duplicates in the complete list. The function should return False otherwise.

# loop through nums
# for each element check for duplicates within k distance
# def has_duplicates(nums_p6, k_p6):
#     # check for k > len(list) return True if true else False
#     for i in range(0, len(nums_p6)):
#         if i - k_p6 < 0 :
#            if nums_p6[i] in nums_p6[0: i-1] or nums_p6[i] in nums_p6[i+1: i+k_p6]:
#                return True
#         elif i + k_p6 >= len(nums_p6):
#             if nums_p6[i] in nums_p6[i-k_p6: i-1] or nums_p6[i] in nums_p6[i+1: len(nums_p6)-1]:
#                 return True

        
# def has_duplicates(nums, k):
#     seen = set()

#     for i in range(len(nums)):
#         if nums[i] in seen:
#             return True

#         seen.add(nums[i])

#         # keep window size ≤ k
#         if len(seen) > k:
#             seen.remove(nums[i - k])

#     return False
# STUDY THIS SET VERSION

 
# ==============================


# Problem 7: Make Pairs
# Write a function divide_list() that takes in an integer list nums 
# consisting of 2*n integers as parameters. The function divides nums into n pairs such that:

# Each element belongs to exactly one pair
# The elements present in a pair are equal
# Return True if nums can be divided into n pairs, otherwise return False

# def divide_list(nums_p7):
#     if len(nums_p7) % 2 != 0:
#         return False
#     pairs = {}
#     for num in nums_p7:
#         if num not in pairs:
#             pairs[num] = 1
#         else:
#             pairs[num] += 1
#     for key, value in pairs.items():
#         if value % 2 != 0:
            
#             return False
    
    
#     return True


# nums1_p7 = [3, 2, 3, 2, 2, 2]
# print(divide_list(nums1_p7))

# nums2_p7 = [1, 2, 3, 4]
# print(divide_list(nums2_p7))

# nums3_p7 = [1, 2, 3, 4, 5]
# print(divide_list(nums3_p7))

# nums4_p7 = [1,1,1,1,1,1,1,1,1,1]
# print(divide_list(nums4_p7))