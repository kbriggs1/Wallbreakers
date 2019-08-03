class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m=[0]
        def helper(root):
            if root==None:
                return 0
            left_height=helper(root.left)
            right_height=helper(root.right)
            m[0]=max(m[0],left_height+right_height)
            return (max(left_height,right_height)+1)
        helper(root)
        return m[0]
