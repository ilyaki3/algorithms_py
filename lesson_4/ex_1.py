"""
Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке:
https://leetcode.com/problems/min-stack/

155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1 or val < self.min:
            self.min = val

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            removed = self.stack.pop()
            if len(self.stack) == 0:
                self.min = None
                return removed
            elif removed == self.min:
                self.min = self.stack[0]
                for el in self.stack:
                    if el < self.min:
                        self.min = el
            return removed

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Success
Details 
Runtime: 48 ms, faster than 99.71% of Python3 online submissions for Min Stack.
Memory Usage: 17.9 MB, less than 83.72% of Python3 online submissions for Min Stack.
"""
