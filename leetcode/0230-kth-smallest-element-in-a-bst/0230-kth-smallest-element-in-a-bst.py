# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = 0
        def inorder(root):
            if not root or self.count == k:
                return
            
            inorder(root.left)

            self.count += 1

            if self.count == k:
                self.answer = root.val
                return
            
            inorder(root.right)

        inorder(root)

        return self.answer
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna