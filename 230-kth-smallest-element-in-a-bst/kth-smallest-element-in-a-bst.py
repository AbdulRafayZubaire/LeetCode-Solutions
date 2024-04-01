# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        number = 0
        count = k

        def helper(root):
            nonlocal count
            nonlocal number
            if not root:
                return
            helper(root.left)
            print(root.val)
            count-=1
            if count == 0:
                number = root.val
                return
            helper(root.right)
        helper(root)
        return number
