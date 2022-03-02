# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #use recursive dfs to go through the tree, once the bottom is reached, work from bottom up,
        #adding 1 everytime we move up. when we get to an intersection of nodes, compare the left and right
        #depth, and take the larger value. repeat the process until the real root is reached
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
