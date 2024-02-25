# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        left_pairs = []
        max_sum = -sys.maxsize

        slow, fast = head, head
        while fast and fast.next:
            left_pairs.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        print(left_pairs)

        while slow:
            max_sum = max(left_pairs.pop() + slow.val, max_sum)
            slow = slow.next
        print(max_sum)
        return max_sum