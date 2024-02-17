# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        count = 0

        while fast.next != None:
            fast = fast.next
            if count >= n:
                slow = slow.next
            count += 1

        slow.next = slow.next.next
        fast = None

        return dummy.next