class MyQueue:

    def __init__(self):
        """
        Initialize two stacks:
        - stack_in is used for enqueue (push)
        - stack_out is used for dequeue (pop)
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        Just append it to stack_in.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns it.
        If stack_out is empty, move all elements from stack_in to stack_out.
        """
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element of the queue without removing it.
        Use pop() to retrieve, then push it back to stack_out.
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        Return True if both stack_in and stack_out are empty.
        """
        return not (self.stack_in or self.stack_out)