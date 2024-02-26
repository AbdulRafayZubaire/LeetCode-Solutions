# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leafPrint(root, leafs):
            if not root:
                return
            # print(root.val)
            
            if not root.left and not root.right:
                leafs.append(root.val)
            else:
                leafPrint(root.left, leafs)
                leafPrint(root.right, leafs)
            
            return leafs

        leafValues1 = leafPrint(root1, [])
        leafValues2 = leafPrint(root2, [])

        return leafValues1 == leafValues2
        