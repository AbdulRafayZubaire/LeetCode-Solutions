# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        list_dic ={}

        p = ListNode(0)
        p.next = head

        i = 0
        while p != None:
            if p not in list_dic:
                list_dic[p] = (p, i)
            else:
                return list_dic[p][0]
            i += 1
            p = p.next
        return None