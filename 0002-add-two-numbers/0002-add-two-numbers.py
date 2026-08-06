# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1_str=""
        num2_str=""
        cur=l1
        while cur:
            num1_str = str(cur.val)+num1_str
            cur=cur.next
        cure =l2
        while cure:
            num2_str = str(cure.val)+num2_str
            cure=cure.next
        total=int(num1_str or 0) + int(num2_str or 0)
        dummy = ListNode(0)
        curr=dummy
        if total==0:
            return ListNode(0)
        for i in reversed(str(total)):
            curr.next=ListNode(int(i))
            curr = curr.next
        return dummy.next