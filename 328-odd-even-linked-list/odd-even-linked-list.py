# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        even = head.next
        even_ptr = head.next
        odd = head
        last_odd = None
        while even and odd:
            if odd.next:
                odd.next = odd.next.next
            if even.next:
                even.next = even.next.next

            last_odd = odd
            odd = odd.next
            even = even.next

        if odd:
            last_odd = odd
        last_odd.next = even_ptr
        return head