from collections import Counter, defaultdict, deque
import time


# Q1. When would you use a set instead of a list? Give two real-world examples where sets are the better choice.


def q1_set_vs_list():
    print("\nQ1: Set vs List")

    customer_ids = [101, 102, 103, 101, 104, 102]

    print("Original List:", customer_ids)

    unique_customer_ids = set(customer_ids)

    print("Unique IDs using Set:", unique_customer_ids)

    if 103 in unique_customer_ids:
        print("Customer ID 103 exists")

    print("\nReal-world Examples:")
    print("1. Unique customer mobile numbers")
    print("2. Unique employee IDs")

    print("\nWhy Set?")
    print("- Removes duplicates automatically")
    print("- Fast membership testing O(1)")


# Q2. What is the time complexity of checking if an element exists in: (a) a list, (b) a set, (c) a dictionary? Why are they different?


def q2_membership_complexity():
    print("\nQ2: Membership Check Complexity")


    numbers_list = list(range(100000))
    numbers_set = set(numbers_list)
    numbers_dict = {i: True for i in numbers_list}

    target = 99999

    start = time.time()
    target in numbers_list
    list_time = time.time() - start

    start = time.time()
    target in numbers_set
    set_time = time.time() - start

    start = time.time()
    target in numbers_dict
    dict_time = time.time() - start

    print("List Lookup Time:", list_time)
    print("Set Lookup Time:", set_time)
    print("Dictionary Lookup Time:", dict_time)

    print("\nComplexities:")
    print("List       -> O(n)")
    print("Set        -> O(1) Average")
    print("Dictionary -> O(1) Average")

# Q3. Write a function using Counter that finds the most common character in a string and returns it with its count.

def most_common_character(text):
    counter = Counter(text)

    char, count = counter.most_common(1)[0]

    return char, count



# Q4. Given two lists of user IDs, write a function that returns IDs present in both lists. What is the most efficient approach?


def common_user_ids(list1, list2):
    return list(set(list1) & set(list2))


# Q5. Why is deque preferred over list for implementing a queue? What specific operation makes the difference?


def q5_deque_example():
    print("\nQ5: deque Example")

    queue = deque()

    queue.append("User1")
    queue.append("User2")
    queue.append("User3")

    print("Queue:", queue)

    served = queue.popleft()

    print("Served:", served)
    print("Remaining Queue:", queue)

    print("\nReason:")
    print("deque.popleft() = O(1)")
    print("list.pop(0) = O(n)")



# Q6. Write a function that groups a list of words by their first letter using defaultdict. Example: ['apple','avocado','banana'] → {'a':['apple','avocado'], 'b':['banana']}

def group_words(words):
    grouped = defaultdict(list)


    for word in words:
        grouped[word[0]].append(word)

    return dict(grouped)



# Q7. What happens when you use a mutable object (like a list) as a dictionary key? Why?


def q7_mutable_key():
    print("\nQ7: Mutable Dictionary Key")


    try:
        my_dict = {}
        my_dict[[1, 2, 3]] = "Invalid"

    except TypeError as e:
        print("Error:", e)

    print("\nReason:")
    print("Lists are mutable and unhashable.")
    print("Dictionary keys must be immutable and hashable.")



# Q8. Write a function that removes all duplicates from a list while preserving the original order of first occurrences.




def remove_duplicates(items):
    seen = set()
    result = []


    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Main Program

if __name__ == "__main__":

    q1_set_vs_list()

    q2_membership_complexity()

    print("\nQ3: Most Common Character")
    character, count = most_common_character("programming")

    print("Character:", character)
    print("Count:", count)

    print("\nQ4: Common User IDs")

    users1 = [101, 102, 103, 104]
    users2 = [103, 104, 105, 106]

    print(common_user_ids(users1, users2))

    q5_deque_example()

    print("\nQ6: Group Words")

    words = ["apple", "avocado", "banana"]

    print(group_words(words))

    q7_mutable_key()

    print("\nQ8: Remove Duplicates While Preserving Order")

    sample = [1, 2, 3, 2, 4, 1, 5]

    print("Original:", sample)
    print("Result:", remove_duplicates(sample))