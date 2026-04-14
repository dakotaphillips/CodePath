# Problem Set Version 2

# Problem 1: Is Monotonic

# Write a function is_monotonic() that takes in a list nums as a parameter and 
# checks if it is either monotone increasing or monotone decreasing.
# A list is monotone increasing if every element is either greater than or equal to the element before it.
# A list is monotone decreasing if every element is either less than or equal to the element before it.
# The function should return True if the given list is either monotone increasing or decreasing and False otherwise.
# Hint: This is a lists problem

# def is_monotonic(nums):
#     sorted_nums = sorted(nums)
#     r_sorted_nums = sorted(nums, reverse=True)

#     if nums == sorted_nums or nums == r_sorted_nums:
#         return True
#     else:
#         return False



# nums1 = [1,2,2,3,10]
# print(is_monotonic(nums1))

# nums2 = [12,9,8,3,1]
# print(is_monotonic(nums2))

# nums3 = [1,1,1]
# print(is_monotonic(nums3))

# nums4 = [1,9,8,3,5]
# print(is_monotonic(nums4))

# Example Output:
# True
# True
# True
# False

# ----------------------------------------------------------------------------------
# Problem 2: Student Directory

# Write a function student_directory() that takes a list of student_names 
# as a parameter and returns a dictionary of students, where each student 
# in student_names is a key mapped to a unique numerical ;' ID.

# def student_directory(student_names):
#     student_dict = {}
#     student_id = 1
#     for student in student_names:
#          student_dict[student] = student_id
#          student_id += 1
#     return student_dict
         
# student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
# print(student_directory(student_names))
# Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}

# ----------------------------------------------------------------------------------
# Problem 3: Dictionary Description

# The following function get_description() takes in a dictionary info 
# and a list keys as parameters. For each key in keys, the function 
# prints the value associated with that key in info and prints None 
# if the key does not exist in info.

# However, the function has a bug! Copy the function into your IDE 
# and run the code. Work with your group members to find the cause 
# of the bug and correctly implement the function.

# def get_description(info, keys):
#     for key in keys:
#         if key in info:
#             print(info[key])
#         else:
#             print("None")
            


# info = {"name": "Tom", "age": "30", "occupation": "engineer"}
# keys = ["name", "occupation", "salary"]
# get_description(info, keys)

# Expected Output:
# Tom
# engineer
# None

# -----------------------------------------------------------------------------------
# Problem 4: Sum Even Values

# Write a function sum_even_values() that returns the sum of all 
# even values in a given dictionary. Assume the dictionary values are all integers.

# instantiate a sum var set to 0
# loop through the dict and retrieve keys, and values
# check if value is even, use value mod 2 == 0
# if true, sum += value
# outside loop return sum_val

# def sum_even_values(dictionary):
#     sum_val = 0
#     for key, value in dictionary.items():
#         if value % 2 == 0:
#             sum_val += value
#     return sum_val


# dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
# print(sum_even_values(dictionary))

# Example Output: 14

# -----------------------------------------------------------------------------------
# Problem 5: Merge Catalogs

# Write a function merge_catalogs() that combines two product catalogs, 
# catalog1 and catalog2 as parameters. Each parameter is a dictionary 
# where each key-value pair represents a product name and its price, 
# respectively. If the same product exists in both catalogs, the price 
# from the second catalog should overwrite the price in the first. 
# Return the updated first catalog dictionary.

# combine both catalogs
# if an item in cat2 doesnt exist in cat1, then add it
# if it does, overwrite the first price with the value if the second one
# return the first one
# 
# forloop over catalog2
# get key value pair
# add them to catalog1
# return catalog1
#
#  

# Example Output: {'apple': 1.0, 'banana': 0.75, 'cherry': 1.25}

# ------------------------------------------------------------------------------------
# Problem 6: Items to Restock

# Write a function get_items_to_restock() that takes in a dictionary 
# products that maps product names to their quantities and an integer 
# restock_threshold as parameters. The function returns a list of 
# products that have a value less than restock_threshold and need to 
# be restocked. If products is empty, the function return an empty list.

# def get_items_to_restock(products, restock_threshold):
#     restock = []
#     for product, quantity in products.items():
#         if quantity < restock_threshold:
#             restock.append(product)
#     return restock


# products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
# restock_threshold = 5
# products2 = {}
# print(get_items_to_restock(products, restock_threshold))
# print(get_items_to_restock(products2, restock_threshold))
# Example Output: ['Product2', 'Product4']

# -----------------------------------------------------------------------------------------
# Problem 7: Best Movie Genre

# Imagine you're contributing to a move recommendation engine, and you're tasked 
# with writing a function named most_popular_genre() that returns the genre with 
# the highest average rating across all movies.

# The function takes in a list of dictionaries named movies as a parameter. 
# Each dictionary represents data associated with a movie, including its title, 
# genre, and rating. The function calculates the average rating for each genre 
# and returns the genre with the highest average rating.

#  

# Example Output: Science Fiction

# --------------------------------------------------------------------------------------------
# Problem 8: Quality Control

# Write a function quality_control() that takes in a dictionary product_scores and an 
# integer threshold as parameters. The dictionary product_scores has key-value pairs 
# that represent a product ID and its quality rating.
# If the product has a score greater than or equal to threshold, the function categorizes it as a "pass".
# If the product has a score less than threshold, the function categorizes it as a "fail".
# The function returns a new dictionary where the key-value pair is the product ID and whether it is a "pass" or "fail".

# def quality_control(product_scores, threshold):
#     pass_fail = {}
#     for product, score in product_scores.items():
#         if score >= threshold:
#             pass_fail[product] = "pass"
#         else: 
#             pass_fail[product] = "fail"
#     return pass_fail

# product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
# threshold = 60
# print(quality_control(product_scores, threshold))

# Example Output: {'x0123': 'pass', 'x0124': 'fail', 'x0125': 'pass', 'x0126': 'fail'}

