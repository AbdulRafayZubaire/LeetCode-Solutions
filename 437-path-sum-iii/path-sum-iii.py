# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        self.dfs(root, targetSum)

        return self.count

    def dfs(self, root, target):
        if not root:
            return

        self.dfs2(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        

    def dfs2(self, root, target):
        if not root:
            return 0
        if target == root.val:
            self.count += 1
        self.dfs2(root.left, target - root.val)
        self.dfs2(root.right, target - root.val)