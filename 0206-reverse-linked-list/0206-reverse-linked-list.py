# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        pre=None
        while cur:
            temp=cur.next#save cur next node
            cur.next=pre#reverse
            #renew
            pre=cur
            cur=temp
        return pre