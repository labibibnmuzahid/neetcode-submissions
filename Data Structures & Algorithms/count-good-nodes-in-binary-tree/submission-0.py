# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Recursive DFS, calculate each node and compare its value to the max updated value, Compare with x node, add number and then return that number
        # Time Complexity - Big O(n), Memory Complexity - Big O(n)

        def dfs(node, maxVal):
            # Edge Case if node is null
            if not node: 
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)