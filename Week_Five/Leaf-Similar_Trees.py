class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.helper(root1) == self.helper(root2)
    def helper(self, root):
        if root:
            stack = []
            temp = []
            stack.append(root)
            while stack:
                curr = stack.pop()
                if not curr.left and not curr.right:
                    temp.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        return temp
