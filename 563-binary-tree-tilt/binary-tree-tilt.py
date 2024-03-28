# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.tilt = 0
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def travel(root):
            if not root:
                return 0
            if not root.left and not root.right:
                root.tilt = 0
                return root.val
            left, right = 0, 0
            left += travel(root.left)
            right += travel(root.right)

            root.tilt = abs(left - right)
            return root.val + left + right

        count = 0
        def traversal(root):
            nonlocal count

            if not root:
                return 0

            traversal(root.left)
            count += root.tilt
            traversal(root.right)
        
        travel(root)
        traversal(root)
        print(count)
        
        return count
