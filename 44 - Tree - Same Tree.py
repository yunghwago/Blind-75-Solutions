# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = True
        #run recursive DFS until different node is found
        #handle base cases 
        if not p and not q: #both trees are null
            return True
        
        #one of the trees is null, or current p node is not the same as current q node
        if not p or not q or p.val != q. val:
            return False

        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) #how tf does this work? 
        #if p and q are unequal at any point in time, the DFS process is cut short by the return False statement above
        #if they are equal all the way through, then True will be returned
