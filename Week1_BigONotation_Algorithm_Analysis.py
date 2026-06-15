import pandas as pd
import math


# Q1: What is the time complexity of accessing the 5th element of a Python list? Explain why.
def access_fifth_element():
    nums = [10, 20, 30, 40, 50, 60, 70]
    return nums[4]


# Q2: Analyze this code and state its Big O:
def mystery(n):
    for i in range(n):
        for j in range(n):
            print(i + j)


# Q3: Given a sorted array of 1 million elements, how many steps (maximum) does binary search need? Show your calculation
def binary_search_steps(n):
    return math.ceil(math.log2(n))


# Q4: Write a function that checks if a string is a palindrome. What is its time complexity? What is its space complexity?
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


# Q6: Rewrite this O(n²) duplicate-check to O(n) using a different data structure:
def has_dup(arr):
    seen = set()

    for item in arr:
        if item in seen:
            return True
        seen.add(item)

    return False


if __name__ == "__main__":

    print("Q1:", access_fifth_element())
    print("Time Complexity: O(1)")
    print()

    print("Q2: O(n²)")
    print("Two nested loops each execute n times.")
    print()

    print("Q3:", binary_search_steps(1_000_000), "steps")
    print()

    print("Q4:", is_palindrome("madam"))
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")
    print()

    print("Q5 Ranking:")
    complexities = [
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)",
        "O(n²)",
        "O(2ⁿ)",
        "O(n!)"
    ]

    for c in complexities:
        print(c)

    print()

    print("Q6:", has_dup([1, 2, 3, 4, 2]))
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")
    print()

    print("Q7:")
    print("Merge Sort Space Complexity = O(n)")
    print("Quick Sort Space Complexity = O(log n) average")
    print()

    print("Q8:")
    linear_time = 5  # ms
    n = 1000

    quadratic_time = linear_time * n

    print(f"O(n): {linear_time} ms")
    print(f"O(n²): {quadratic_time} ms = {quadratic_time/1000} seconds")