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
                return -1
            if not root.left and not root.right:
                return 0
            
            left = 1 + height(root.left)
            right = 1 + height(root.right)
            count = max(left+right, count)
            return max(left, right)

        height(root)
        return count 