class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        if not root.children: return [root.val]
        l = []
        for c in root.children: l += self.postorder(c)
        return l + [root.val]
