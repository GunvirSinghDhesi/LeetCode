# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if node:
                leftPath = longest_path(node.left)
                rightPath = longest_path(node.right)
                nonlocal diameter
                diameter = max(diameter, leftPath+rightPath)
                return max(leftPath, rightPath)+1
            else: # reached the leaf node
                return 0

        
            

        longest_path(root)
        return diameter
