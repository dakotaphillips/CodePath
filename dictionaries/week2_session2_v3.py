# ==============================
# Problem Set Version 3 (No Conflicts)
# ==============================


# Problem 1: Return Book
# Increment book count or add if not present.

def return_book(book_title_p1, library_map_p1):
    pass


library_map_p1 = {
    "The Hobbit": 2,
    "1984": 1,
    "The Great Gatsby": 4
}

updated_lib_p1_a = return_book("1984", library_map_p1)
print(updated_lib_p1_a)

updated_lib_p1_b = return_book("The Giver", library_map_p1)
print(updated_lib_p1_b)


# ==============================


# Problem 2: Dictionary Difference
# Return key-value pairs only in first dict, not in second.

def dict_difference(dict_one_p2, dict_two_p2):
    pass


dict_one_p2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two_p2 = {'b': 2, 'd': 1}

diff_result_p2 = dict_difference(dict_two_p2, dict_one_p2)
print(diff_result_p2)


# ==============================


# Problem 3: Take from Stock
# Remove quantity if possible, handle errors.

def pop_stock(items_map_p3, item_name_p3, quantity_p3):
    pass


items_map_p3 = {
    "chocolate": 20,
    "candy": 5,
    "chips": 10
}

resultA_p3 = pop_stock(items_map_p3, "candy", 2)
resultB_p3 = pop_stock(items_map_p3, "candy", 5)
resultC_p3 = pop_stock(items_map_p3, "lollipops", 5)
resultD_p3 = pop_stock(items_map_p3, "chocolate", 5)

print(resultA_p3)
print(resultB_p3)
print(resultC_p3)
print(resultD_p3)


# ==============================


# Problem 4: Group By Frequency
# Map frequency -> list of elements.

def group_by_frequency(input_list_p4):
    pass


input_list_p4 = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']

grouped_result_p4 = group_by_frequency(input_list_p4)
print(grouped_result_p4)


# ==============================


# Problem 5: No Duplicates Allowed
# Keep unique elements based on last occurrence order.

def remove_duplicates_from_front(nums_list_p5):
    pass


nums_list_p5 = [6, 5, 3, 5, 2, 8, 3]

unique_result_p5 = remove_duplicates_from_front(nums_list_p5)
print(unique_result_p5)


# ==============================


# Problem 6: First Repeating Element
# Return smallest index of element that repeats.

def find_min_index_of_repeating(nums_list_p6):
    pass


nums_case1_p6 = [5, 6, 3, 4, 3, 6, 4]
nums_case2_p6 = [5, 6, 3, 4]
nums_case3_p6 = [5, 6, 2, 4, 3, 4, 3]

print(find_min_index_of_repeating(nums_case1_p6))
print(find_min_index_of_repeating(nums_case2_p6))
print(find_min_index_of_repeating(nums_case3_p6))


# ==============================


# Problem 7: Target Sum
# Return indices of two numbers adding to target.

def two_sum(nums_list_p7, target_value_p7):
    pass


nums_case1_p7 = [2, 7, 11, 15]

q1_result_p7 = two_sum(nums_case1_p7, 9)
q2_result_p7 = two_sum(nums_case1_p7, 18)

nums_case2_p7 = [3, 3]

q3_result_p7 = two_sum(nums_case2_p7, 6)

print(q1_result_p7)
print(q2_result_p7)
print(q3_result_p7)