# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def recursive(root, string, result):
            if not root:
                return
            string += str(root.val)
            if not root.left and not root.right:
                result.append(string)
                return result
            string += '->'

            recursive(root.left, string, result)
            recursive(root.right, string, result)

            return result
        
        return recursive(root, "", [])