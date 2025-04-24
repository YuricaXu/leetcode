# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        pre=head
        cur=head.next
        next=head.next.next

        cur.next=pre#exchange
        pre.next=self.swapPairs(next)#exchange head

        return cur