# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        instinct: for every node, compare L and R to the root
        this solution doesn't work
        why?
        ex. binary search tree containing:
           5
           /\
          3  7
             /\
            4 8
        3 is less than 5, and 7 is greater than 5
        4 is less than 7, and 8 is greater than 7
        but 4 is greater than 5 and it's ultimately to the right of it
        instead of checking 4 < 7, we need to check for if (5 < 4 < 7)
        
        what data structure will help us here?
        we could have a list of previous roots, and store all previous roots, and call the minimum of the root, but that doesn't seem to make sense algorithmically
        
        """
        #checks a single node to see if it's value falls under the bounds defined by the nodes that came before it
        def isValid (node, left, right):
            if not node:
                return True #null is always an acceptable child node
            if not (node.val > left and node.val < right):
                return False
            return (isValid(node.left, left, node.val) and #move down and to the left of the tree. the left boundary stays the same, 
                                                                #because the node to the left should be smaller
                                                                #the node we have right now, and we want to retain the tightest bound possible for our comparison
                                                                #node.val is also guaranteed to be smaller than right's value
                    isValid(node.right, node.val, right))
        return isValid(root, float("-inf"), float(inf)) #convert neg and pos infinity to number
