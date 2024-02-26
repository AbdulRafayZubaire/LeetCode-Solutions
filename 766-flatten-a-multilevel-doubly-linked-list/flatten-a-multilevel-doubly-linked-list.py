"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        start = Node(0, None, head, None)
        prev = start
        stack = [head]

        while stack:
            curr = stack.pop()

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev.next = curr
            curr.prev = prev
            prev = curr


        start.next.prev = None
        return start.next

       