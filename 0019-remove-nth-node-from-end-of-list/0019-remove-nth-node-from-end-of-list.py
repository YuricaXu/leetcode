# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create a head
        dummy_head = ListNode(0, head)

        #create 2 nodes:fast and slow
        slow = fast = dummy_head

        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next=slow.next.next#renew n-1 node to delete n node

        return dummy_head.next