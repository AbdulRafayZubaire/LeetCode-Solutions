# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        p = None
        q = head
        r = q.next
        count = 1
        
        while True:
            q.next = p
            p = q
            q = r
            if count % k == 0:
                temp_count = 0
                temp_ptr = q
                while temp_ptr and temp_count < k:
                    temp_ptr = temp_ptr.next
                    temp_count += 1
                if temp_count < k: 
                    head.next = q
                else:
                    head.next = self.reverseKGroup(q, k)
                return p
            if not q:
                return p 

            r = r.next
            count += 1
