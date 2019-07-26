# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        numbers = []
		#Store all the values of the lists of nodes in numbers 
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                numbers.append(cur.val)
                cur = cur.next
		#Sort all the numbers
        numbers.sort()
		#Initialize two variables to point to a node with the value 'None'.
		#A dummy variable is being created so that you can return dummy.next
		#(which will contain the head of list) after you create your list of nodes. 
        cur = dummy = ListNode(None)
		#Create the list of nodes
        for num in numbers:
            cur.next = ListNode(num)
            cur = cur.next
		#dummy.next contains reference to the head of the list
        return dummy.next
