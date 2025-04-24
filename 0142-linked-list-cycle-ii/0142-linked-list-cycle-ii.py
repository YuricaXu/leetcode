# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()# Use a set to store visited nodes
        
        while head:
            # If the current node has been visited before,
            # it means we've found the start of the cycle
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None