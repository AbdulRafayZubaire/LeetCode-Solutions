# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        count = 0

        while p != None:
            p = p.next
            count += 1

        if count == n:
            temp = head
            if head.next != None:
                head = None
                head = temp.next
            else:
                head = None
            return head

        i = 0
        p = head
        q = p
        while i != (count - n):
            q = p
            p = p.next
            i += 1
        if p != None or p.next != None:
            q.next = p.next
            p = None

        return head