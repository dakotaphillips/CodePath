# ==============================
# Problem Set Version 2 (No Conflicts)
# ==============================


# Problem 1: Update Score
# Add points to a player. If player doesn't exist, add them.

def update_score(score_map_p1, player_name_p1, points_p1):
    pass


score_map_p1 = {"Alice": 100, "Bob": 90}

update_score(score_map_p1, "Alice", 10)
print(score_map_p1)

update_score(score_map_p1, "Calvin", 20)
print(score_map_p1)

update_score(score_map_p1, "Calvin", 5)
print(score_map_p1)


# ==============================


# Problem 2: Dictionary Intersection
# Return a new dict with key-value pairs found in both dictionaries.

def dict_intersection(dict_a_p2, dict_b_p2):
    pass


dict_a_p2 = {'a': 1, 'b': 2, 'c': 3}
dict_b_p2 = {'b': 2, 'c': 4}

result_dict_p2 = dict_intersection(dict_a_p2, dict_b_p2)
print(result_dict_p2)


# ==============================


# Problem 3: Filter by Price
# Remove items below threshold and return removed items list.

def remove_items_below_price(items_map_p3, threshold_p3):
    pass


items_map_p3 = {
    "apple": 1.99,
    "banana": 0.99,
    "cherry": 3.49,
    "date": 0.69
}

removed_list_p3_a = remove_items_below_price(items_map_p3, 1.00)
print(removed_list_p3_a)

removed_list_p3_b = remove_items_below_price(items_map_p3, 1.00)
print(removed_list_p3_b)


# ==============================


# Problem 4: Find Odd Occurrences
# Find two numbers that occur odd number of times.

def find_odd_occurrences(numbers_list_p4):
    pass


numbers_list_p4 = [1, 4, 2, 3, 2, 3, 3, 4, 4, 4]

odd_result_p4 = find_odd_occurrences(numbers_list_p4)
print(odd_result_p4)


# ==============================


# Problem 5: Find Mode
# Return most frequent element; if tie, return first appearing.

def find_mode(values_list_p5):
    pass


values_list_p5 = [1, 2, 3, 2, 3, 3, 4, 4, 4, 4]

mode_result_p5 = find_mode(values_list_p5)
print(mode_result_p5)


# ==============================


# Problem 6: How Many Smaller
# For each number, count how many numbers are smaller.

def smaller_numbers_than_current(nums_list_p6):
    pass


nums_list_p6 = [6, 1, 2, 2, 3]

smaller_counts_p6 = smaller_numbers_than_current(nums_list_p6)
print(smaller_counts_p6)


# ==============================


# Problem 7: Good Pairs
# Count number of good pairs (i < j and nums[i] == nums[j])

def num_identical_pairs(nums_list_p7):
    pass


nums_case1_p7 = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums_case1_p7))

nums_case2_p7 = [1, 2, 3]
print(num_identical_pairs(nums_case2_p7))

nums_case3_p7 = [1, 1, 1, 1]
print(num_identical_pairs(nums_case3_p7))