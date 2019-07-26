class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leftSum = 0
        
        def dfs(root):
            if not root:
                return

            if root.left and not root.left.left and not root.left.right:
                nonlocal leftSum
                leftSum += root.left.val
                
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return leftSum
