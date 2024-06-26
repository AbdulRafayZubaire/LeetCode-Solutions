# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inOrder(root):
            nonlocal prev
            if not root:
                return True
            if not inOrder(root.left):
                return False
            if root.val <= prev:
                return False
            prev = root.val
            return inOrder(root.right)
            
        prev = -sys.maxsize
        return inOrder(root)