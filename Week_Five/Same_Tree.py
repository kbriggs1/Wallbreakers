class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node1, node2):
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        return dfs(p, q)
        
