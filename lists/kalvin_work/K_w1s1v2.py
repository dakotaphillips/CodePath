
# Problem Set Version 2

#-------------------------------------------------------------------------------------------

# Problem 1: Hello User!
# Write a function greet_user() that takes in a string name as a parameter and prints "Hello <name>".

# def greet_user(name):
#     pass
# Example Input: Michael
# Example Output: Hello Michael

# Note: pass is a keyword that is used as a placeholder for future code

# def greet_user(name):
#     print(f"Hello {name}")

# name = input("What is your name? ")
# greet_user(name)


# #-------------------------------------------------------------------------------------------

# Problem 2: Calculate Difference
# Write a function difference() that returns the difference between two integers a and b (b should be subtracted from a).

# def difference(a, b):
#     pass
# Example Usage: diff = difference(8, 3)
# Example Output: diff = 5


# def difference(a,b):
#     return a-b

# diff = difference(8,3)
# print(diff)


# #-------------------------------------------------------------------------------------------

# Problem 3: List Concatenation
# Given an integer list nums of length n, create a function concatenate_list() that creates and returns a 
# list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums lists.

# def concatenate_list(nums):
#     pass
# Example Input: [1,2,3,4]
# Example Output: [1,2,3,4,1,2,3,4]

# def concatenate_list(nums):
#     return nums*2

# nums = [1,2,3,4]
# print(concatenate_list(nums))




# #-------------------------------------------------------------------------------------------

# Problem 4: Sleep Assessment
# Write a function sleep_assessment() that takes in an integer parameter hours indicating the number of hours the user slept.
# If hours is less than 8, print "Oof, go back to bed!".
# If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
# If hours is greater than 10, print "You're a sleep prodigy!".

# def sleep_assessment(hours):
#     pass
# Example Usage:

# sleep_assessment(10)
# sleep_assessment(4)
# sleep_assessment(12)
# sleep_assessment(9)
# Example Output:

# You got a good night's rest!
# Oof, go back to bed!
# You're a sleep prodigy!
# You got a good night's rest!


# def sleep_assessment(hours):
#     if hours < 8:
#         print("Oof, go back to bed!")
#     elif hours >= 8 and hours <= 10:
#         print("You got a good night's rest!")
#     else:
#         print("You're a sleep prodigy!")


# sleep_assessment(10)
# sleep_assessment(4)
# sleep_assessment(12)
# sleep_assessment(9)


# #-------------------------------------------------------------------------------------------

# Problem 5: Calculate Tip
# Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
# If service_quality is "poor", the function should return 10% of the bill value.
# If service_quality is "average", the function should return 15% of the bill value.
# If service_quality is "excellent", the function should return 20% of the bill value.
# If service_quality is any other value, the function should return None.

# def calculate_tip(bill, service_quality):
#     pass
# Example Usage:

# tip1 = calculate_tip(44.53, "average")
# print(tip1)
# tip2 = calculate_tip(44.53, "poor")
# print(tip2)
# tip3 = calculate_tip(44.53, "excellent")
# print(tip3)
# Example Output:

# 6.6795
# 4.453
# 8.906


# def calculate_tip(bill, service_quality):
#     if service_quality == "poor":
#         return bill * .1
#     elif service_quality == "average":
#         return bill * .15
#     elif service_quality == "excellent":
#         return bill * .2
#     else:
#         return None

# tip1 = calculate_tip(44.53, "average")
# print(tip1)
# tip2 = calculate_tip(44.53, "poor")
# print(tip2)
# tip3 = calculate_tip(44.53, "excellent")
# print(tip3)


# #-------------------------------------------------------------------------------------------

# Problem 6: Rock, Paper, Scissors
# Write a function rock_paper_scissors() that determines the winner of a game of Rock, Paper, Scissors. The function accepts two strings as parameters: 
# player1 and player2. Each parameter can have a value of "rock", "paper", or "scissors".

# Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
# Rock wins against scissors.
# Scissors wins against paper.
# Paper wins against rock.

# If both player1 and player2 have the same value, print "It's a tie!".

# def rock_paper_scissors(player1, player2):
#     pass
# Example Usage:

# rock_paper_scissors("rock", "rock")
# rock_paper_scissors("scissors", "rock")
# rock_paper_scissors("scissors", "paper")
# rock_paper_scissors("rock", "paper")
# rock_paper_scissors("paper", "rock")
# Example Output:

# It's a tie!
# Player 2 wins!
# Player 1 wins!
# Player 2 wins!
# Player 1 wins!

# import random

# choices = ["rock", "paper", "scissors"]

# p1_score = 0
# computer_score = 0
# done = False


# def rock_paper_scissors(player_choice, computer_choice):
#     global p1_score, computer_score

#     if player_choice == computer_choice:
#         print("This one's a DRAW!!!!")

#     elif player_choice == "rock" and computer_choice == "scissors":
#         print("Good Job!")
#         p1_score += 1

#     elif player_choice == "paper" and computer_choice == "rock":
#         print("Good Job!")
#         p1_score += 1

#     elif player_choice == "scissors" and computer_choice == "paper":
#         print("Good Job!")
#         p1_score += 1

#     else:
#         print("You lost this round!")
#         computer_score += 1

#     print(f"Score → You: {p1_score} | Computer: {computer_score}")




# while not done and p1_score < 3 and computer_score < 3:

#     player_choice = input("First to 3: ROCK, PAPER, or SCISSORS!!! ").lower()

#     if player_choice in choices:
#         computer_choice = random.choice(choices)
#         print(f"Computer chose: {computer_choice}")
#         rock_paper_scissors(player_choice, computer_choice)

#     elif player_choice == "stop":
#         done = True

#     else:
#         print("Please choose a valid answer.")


# if p1_score > computer_score:
#     print("Game Over! YOU WIN!!!")
# else:
#     print("Game Over!")

# #-------------------------------------------------------------------------------------------

# Problem 7: Unscramble and Divide
# Given the following lines of code, work with your group members to place the lines in order to write and call a function that divides each value in an input list by 2.

# a. result = []
# b. for number in lst:
# c. result.append(halved)
# d. halved = number/2
# e. halve_lst([2,4,6,8])
# f. return result
# g. def halve_lst(lst):


# Example Output: [1,2,3,4]


# def halve_lst(lst):
#     result = []
#     for number in lst:
#         halved = number/2
#         result.append(halved)
#     return result

# print(halve_lst([2,4,6,8]))


# #-------------------------------------------------------------------------------------------

# Problem 8: Above the Threshold
# Write a function above_threshold() that takes in a list of integers lst and an integer threshold as parameters. The function should iterate through the original 
# list and return a new list containing only numbers that are greater than threshold.

# def above_threshold(lst, threshold):
#     pass
# Example Usage:

# lst = [8,2,13,11,4,10,14]
# result = above_threshold(lst, 10)
# print(result)
# Example Output: [13,11,14]

#   

# #-------------------------------------------------------------------------------------------

# Problem 9: Countdown
# Write a function countdown() that takes in two positive integers m and n as parameters and prints numbers from m down to n.

# def countdown(m,n):
#     pass
# Example Usage: countdown(5,1)

# Example Output:

# 5
# 4
# 3
# 2
# 1


# def countdown(m, n):
#     # while loop version
#     # while m >= n:
#     #     print(m)
#     #     m -= 1
#     # for loop version
#     for i in range(m,n-1,-1):
#         print(i)


# countdown(5,1)


#-------------------------------------------------------------------------------------------

# Problem 10: Calculate Power
# Write a function power() that takes in two integers base and exponent. The function should return the value of the base number to the power of the exponent.

# def power(base, exponent):
#     pass
# Example Usage:

# pow1 = power(2,5)
# print(pow1)
# pow2 = power(3,3)
# print(pow2)
# Example Output:

# 32
# 27

# def power(base, exponent):
#     return base**exponent

# pow1 = power(2,5)
# print(pow1)
# pow2 = power(3,3)
# print(pow2)


# #-------------------------------------------------------------------------------------------

# Problem 11: Length of List
# Without using the built-in len() function, write a function list_length() that takes in a list lst as a parameter and returns the length of the list.

# def list_length(lst):
#     pass
# Example Usage:

# lst = [2,4,6,8,10]
# length = list_length(lst)
# print(length)
# Example Output: 5


# def list_length(lst):
#     length = 0
#     for i in lst:
#         length += 1
#     return length

# lst = [2,4,6,8,10]
# length = list_length(lst)
# print(length)


#-------------------------------------------------------------------------------------------

# Problem 12: Calculate Factorial
# Write a function factorial() that takes in an integer n as a parameter and returns its factorial. The factorial of a number is the product of all positive 
# integers less than or equal to that number. For example, the factorial of 5 (denoted as 5!) is 5! = 5 * 4 * 3 * 2 * 1 which equals 120.

# def factorial(n):
#     pass
# Example Usage: print(factorial(3))
# Example Output: 6

# import math
# def factorial(n):
#     # return math.factorial(n)
#     factor = 1
#     for i in range(1, n+1):  # could also use range(n, 0, -1)
#         factor = factor * i
#     return factor


# print(factorial(3))




#-------------------------------------------------------------------------------------------

# Problem 13: Calculate the Squares
# Write a function squares() that takes a list of integers nums as a parameter and returns a new list containing the square of each number in the original list.

# def squares(nums):
#     pass
# Example Input: [1,2,3,4]
# Example Output: [1,4,9,16]

# def squares(nums):
#     new_nums = []
#     for num in nums:
#         new = num*num
#         new_nums.append(new)
#     return new_nums

# print(squares([1,2,3,4]))


#-------------------------------------------------------------------------------------------

# Problem 14: Multiply List
# Write a function multiply_list() that takes in a list of integers lst and an integer multiplier as parameters. 
# The function returns a new list containing each value in lst multiplied by multiplier.

# def multiply_list(lst, multiplier):
#     pass
# Example Usage:

# lst = [1,2,3]
# new_lst = multiply_list(lst, 3)
# Example Output: new_lst = [3,6,9]


# def multiply_list(lst, multiplier):
#     new_lst = []
#     for n in lst:
#         num = n * multiplier
#         new_lst.append(num)
#     return new_lst

# lst = [1,2,3]
# new_lst = multiply_list(lst, 3)
# print(new_lst)

#-------------------------------------------------------------------------------------------

# Problem 15: Count Evens
# Write a function count_evens() that takes in a list of integers lst as a parameter. The function returns the number of even numbers in the list.

# def count_evens(lst):
#     pass
# Example Usage:

# lst1 = [1,5,7,9]
# count1 = count_evens(lst1)
# print(count1)

# lst2 = [2,4,6,8]
# count2 = count_evens(lst2)
# print(count2)
# Example Output:

# 0
# 4


# def count_evens(nums):
#     total = 0
#     for num in nums:
#         if num % 2 == 0:
#             total += 1
#     return total



# lst1 = [1,5,7,9]
# count1 = count_evens(lst1)
# print(count1)

# lst2 = [2,4,6,8]
# count2 = count_evens(lst2)
# print(count2)
