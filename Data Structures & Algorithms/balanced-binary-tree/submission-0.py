# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        #balance = 0
        def dfs(root): # changed from using balance var
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # test cases wouldnt pass until i account for subtree children
            if left is False or right is False:
                return False

            if abs(left-right) > 1:
                return False
            return 1 + max(left, right)

        
        
        
        return dfs(root) is not False


        
        
        