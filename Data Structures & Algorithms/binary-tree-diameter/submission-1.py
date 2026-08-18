# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # i didnt write this, i tried to do the depth solution but it didnt work and the AI auto corrected to this. there is no way this is an easy problem wtf
    
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res

        # Original
    #     class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     return 1 + max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))