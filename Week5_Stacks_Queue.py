##############################################################################################
#1.Implement a MinStack that supports push, pop, top, and getMin, all in O(1) time. Explain your approach.
push(5)
main: [5]
min : [5]

push(3)
main: [5, 3]
min : [5, 3]

push(7)
main: [5, 3, 7]
min : [5, 3]

push(2)
main: [5, 3, 7, 2]
min : [5, 3, 2]

getMin() => 2

pop()

main: [5, 3, 7]
min : [5, 3]

getMin() => 3

Example:-
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)

            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self) -> None:
            if not self.stack:
                raise IndexError("Stack is empty")

            val = self.stack.pop()

            if val == self.min_stack[-1]:
                self.min_stack.pop()

        def top(self) -> int:
            if not self.stack:
                raise IndexError("Stack is empty")
            return self.stack[-1]

        def getMin(self) -> int:
            if not self.min_stack:
                raise IndexError("Stack is empty")
            return self.min_stack[-1]

##############################################################################################

#2.Write a function that evaluates a postfix expression (Reverse Polish Notation). Example: ['2','1','+','3','*'] → 9.
def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()  # second operand
            a = stack.pop()  # first operand

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # truncate toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[-1]

##############################################################################################

#3.Implement a Queue using two Stacks only. Explain the amortized time complexity of the dequeue operation.

	
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue is empty")

        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def front(self):
        if self.empty():
            raise IndexError("Queue is empty")

        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

##############################################################################################

#4.Given an array of daily temperatures [73,74,75,71,69,72,76,73], return an array where each element tells how many days until a warmer temperature. Use a stack.
Day 0 (73) → warmer temperature (74) occurs after 1 day.
Day 1 (74) → warmer temperature (75) occurs after 1 day.
Day 2 (75) → warmer temperature (76) occurs after 4 days.
Day 6 (76) → no warmer day exists → 0

Store indices of temperatures in a stack.

The stack maintains temperatures in decreasing order.

When we encounter a temperature higher than the one at the top of the stack:

    Pop the index from the stack.
    Calculate the distance between the current day and the popped day.
    Store the result.

##############################################################################################
#5.Write a function that uses a stack to convert an infix expression like '3 + 4 * 2' to postfix '3 4 2 * +'.

def infix_to_postfix(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    output = []
    stack = []

    tokens = expression.split()

    for token in tokens:

        # Operand
        if token.isalnum():
            output.append(token)

        # Left parenthesis
        elif token == '(':
            stack.append(token)

        # Right parenthesis
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            stack.pop()  # remove '('

        # Operator
        else:
            while (
                stack and
                stack[-1] != '(' and
                precedence.get(stack[-1], 0) >= precedence[token]
            ):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

return " ".join(output)

##############################################################################################
#6.Explain the difference between LIFO and FIFO with real-world examples. When would you choose a stack over a queue?
1. LIFO (Last In, First Out)
    The last element added is the first one removed.

    This is the behavior of a Stack.

    Real-World Examples
    Stack of Plates
    
2. FIFO (First In, First Out)

    The first element added is the first one removed.

    This is the behavior of a Queue.

    Real-World Examples
    Supermarket Checkout Line

##############################################################################################
#7.Implement a function that checks if a sequence of push/pop operations on a stack is valid. Given pushed=[1,2,3,4,5] and popped=[4,5,3,2,1], return True.

	
def validate_stack_sequences(pushed, popped):
    stack = []
    pop_idx = 0

    for x in pushed:
        stack.append(x)

        while (
            stack and
            pop_idx < len(popped) and
            stack[-1] == popped[pop_idx]
        ):
            stack.pop()
            pop_idx += 1

    return len(stack) == 0

##############################################################################################
#8.Design a MaxStack that supports push, pop, top, peekMax, and popMax. What tradeoffs do you encounter?

	
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]