class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            head.next, head, pre = pre, head.next, head
        return pre
