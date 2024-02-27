# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.maxlen = 0

        # root is a TreeNode, direction is an integer which is either 0(left) or 1(right) and curr_len is current length which is an integer
        def traverse(root, direction, curr_len):
            if not root:
                return
            self.maxlen = max(self.maxlen, curr_len)

            traverse(root.left, 'left', curr_len+1 if direction == 'right' else 1)
            traverse(root.right, 'right', curr_len+1 if direction == 'left' else 1)

        traverse(root, 'left', 0)
        return self.maxlen









    # def longestZigZag(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     self.count = 0

    #     self.dfs(root, {})

    #     return self.count - 1

    # def dfs(self, root, memo):

    #     if not root:
    #         return

    #     count1 = self.left(root)
    #     count2 = self.right(root)

    #     if root in memo:
    #         self.count = memo[root]
    #     else:
    #         self.count = max(self.count, max(count1, count2))
    #     memo[root] = self.count

    #     self.dfs(root.left, memo)
    #     self.dfs(root.right, memo)

    # def right(self, root):
    #     if not root:
    #         return 0
    #     return 1 + self.left(root.left)
    
    # def left(self, root):
    #     if not root:
    #         return 0
    #     return 1 + self.right(root.right)