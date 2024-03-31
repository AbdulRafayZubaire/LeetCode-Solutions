# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def height(root):
            nonlocal count
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            left = height(root.left)
            right = height(root.right)
            count = max(left+right, count)
            return 1 + max(left, right)

        height(root)
        return count 