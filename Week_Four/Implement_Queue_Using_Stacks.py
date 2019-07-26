class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        stack2 = []
        while self.stack:
            stack2.append(self.stack.pop())
        self.stack.append(x)
        while stack2:
            self.stack.append(stack2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
