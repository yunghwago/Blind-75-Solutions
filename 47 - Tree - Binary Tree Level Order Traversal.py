# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        isn't this just a bfs, with a list returned everytime a new depth is reached?
        """
        #base case, empty tree
        if not root:
            return []
        levelList = []
        output = []        
        level = 0 #bfs level that will be returned
        q = deque([root]) #insert root into queue
        #output.append([root.val])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if levelList:
                output.append(levelList)
            levelList = []
        return output
