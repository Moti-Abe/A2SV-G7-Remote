# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            if leftHeight == -1 or rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight) 
        val = dfs(root)
        if val == -1:
            return False
        else:
            return True
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna