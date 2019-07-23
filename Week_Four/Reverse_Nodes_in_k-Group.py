class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (not head) or k < 2:
            return head

        dummy_head = ListNode(0)
        pre = dummy_head
        cur = head
        
        while cur:
            step = k - 1
            start = cur
            while cur and step:
                cur = cur.next
                step -= 1

            if cur and step == 0:
                tmp = cur.next
                cur.next = None
                new_head = self.helper(start)

                pre.next = new_head
                pre = start
                cur = tmp
            else:
                pre.next = start

        return dummy_head.next

    def helper(self, head):
        pre = None
        cur = head

        while cur:
            pre, cur.next, cur = cur, pre, cur.next

        return pre
