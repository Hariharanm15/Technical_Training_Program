
#######################################################################################
#1. Implement a complete LinkedList class with: append, prepend, delete_by_value, search, and print_list methods. Test each method.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Add node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    # Delete first occurrence of a value
    def delete_by_value(self, value):
        if self.head is None:
            return False
        # Delete head node
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    # Search for a value
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
        
    # Print the linked list
    def print_list(self):
        current = self.head

        if current is None:
            print("Empty List")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
        
#######################################################################################
#2.Write a function to reverse a linked list iteratively. Trace through the algorithm step by step for the list 1→2→3→4.
	
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next node

        current.next = prev       # Reverse pointer

        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev

#######################################################################################
#3.Implement Floyd's Cycle Detection algorithm. Explain why the fast pointer moves 2 steps and the slow pointer moves 1 step.

If there is a cycle, the two pointers will eventually meet.

class Node:
def __init__(self, data):
    self.data = data
    self.next = None
    
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        if slow == fast:
            return True
    return False

#######################################################################################		
#4.Write a function to merge two sorted linked lists into one sorted list. What is the time and space complexity?
	
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    # Attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next

#######################################################################################

#5.Given a linked list 1→2→3→4→5, write a function that removes the 2nd node from the end (node 4). Use the two-pointer technique.


class Node:
def __init__(self, data):
    self.data = data
    self.next = None
    
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    # Move both pointers
    while fast:
        fast = fast.next
        slow = slow.next
    # Remove nth node from end
    slow.next = slow.next.next
    return dummy.next

#######################################################################################
#6.Compare arrays vs linked lists: When would you choose a linked list over a Python list? Give specific scenarios.
	
Arrays (Python Lists) vs Linked Lists
Operation	Python List(Dynamic Array)  	Linked List
Access by index	    	O(1)	                   O(n)
Search	            	O(n)	                   O(n)
Insert at beginning		O(n)					   O(1)
Delete at beginning		O(n)					   O(1)
Insert/Delete in middle 
(if node known)			O(n)					   O(1)
Append at end			O(1) amortized			   O(n)*
Memory usage			Lower					Higher (extra pointer per node)
Cache performance		Excellent				Poor

#######################################################################################
#7.Write a function that detects the node where a cycle begins in a linked list (not just whether a cycle exists). Explain the math behind it.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def find_cycle_start(head):
        slow = fast = head
        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle
        # Phase 2: Find cycle entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

#######################################################################################			
#8.Implement a function that checks if a linked list is a palindrome using O(n) time and O(1) extra space. Hint: reverse the second half.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def is_palindrome(head):
        if not head or not head.next:
            return True
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Compare halves
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True