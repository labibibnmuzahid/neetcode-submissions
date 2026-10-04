# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # 1. Base case belongs inside dfs
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
            
            # 2. Indent this return so it is part of the dfs function
            return [balanced, 1 + max(left[1], right[1])]
            
        # 3. Call the dfs function and return the boolean result
        if not root:
            return True
        return dfs(root)[0]