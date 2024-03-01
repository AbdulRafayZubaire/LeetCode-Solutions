# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not postorder or not inorder:
            return None

        rootNode = TreeNode(postorder.pop())
        # return root
        root_index = inorder.index(rootNode.val)
        rootNode.right = self.buildTree(inorder[root_index+1:], postorder)
        rootNode.left = self.buildTree(inorder[:root_index], postorder)

        return rootNode