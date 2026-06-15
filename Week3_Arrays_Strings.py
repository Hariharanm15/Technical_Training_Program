from collections import Counter

# Q1.  Implement the Two Sum problem: Given nums=[2,7,11,15] and target=9, return indices of two numbers that add up to target. What is your solution's time and space complexity?


def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


print("Q1:", two_sum([2, 7, 11, 15], 9))


# Q2. Write a function that finds the longest substring without repeating characters. Example: 'abcabcbb' → 3 ('abc'). Use the sliding window technique.


def longest_substring(s):

    left = 0
    seen = {}
    max_length = 0

    for right in range(len(s)):

        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right

        max_length = max(max_length, right - left + 1)

    return max_length


print("Q2:", longest_substring("abcabcbb"))

# Q3. Explain the two-pointer technique. Write a function that removes duplicates from a sorted array in-place and returns the new length.


def remove_duplicates(nums):

    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:

            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


arr = [1, 1, 2, 2, 3, 4, 4]

length = remove_duplicates(arr)

print("Q3 Length:", length)
print("Q3 Array:", arr[:length])



# Q4. Given an array [1,-2,3,4,-1,2,1,-5,4], find the contiguous subarray with the largest sum (Kadane's algorithm). What is the time complexity?


def max_subarray(nums):

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:

        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum


print("Q4:", max_subarray([1, -2, 3, 4, -1, 2, 1, -5, 4]))



# Q5. Write a function to determine if two strings are anagrams of each other. Provide two different approaches and compare their complexities.


from collections import Counter

def is_anagram_counter(s1, s2):

    return Counter(s1) == Counter(s2)


print("Q5 Counter:", is_anagram_counter("listen", "silent"))


# Q5,2. Anagram Check - Sorting


def is_anagram_sorting(s1, s2):


    return sorted(s1) == sorted(s2)


print("Q5 Sorting:", is_anagram_sorting("listen", "silent"))



# Q6. Implement a function that rotates an array by k positions to the right. Example: [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]. Can you do it in O(1) extra space?



def rotate_array(nums, k):


    k = k % len(nums)

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])

    return nums


print("Q6:", rotate_array([1, 2, 3, 4, 5], 2))


# Q7. Best Time to Buy and Sell Stock: Given prices=[7,1,5,3,6,4], find the maximum profit from one buy and one sell. Write the solution and explain your approach.


def max_profit(prices):

    min_price = float('inf')
    max_profit_value = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit_value = max(max_profit_value, profit)

    return max_profit_value


print("Q7:", max_profit([7, 1, 5, 3, 6, 4]))

# Q8. Write a function that, given a string of parentheses and brackets, checks if it is balanced. Example: '([])' → True, '([)]' → False.


def is_balanced(s):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        elif char in pairs:

            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


print("Q8 Example 1:", is_balanced("([])"))
print("Q8 Example 2:", is_balanced("([)]"))
