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
        def get_num(head):
            num = ""
            current = head

            while current is not None:
                num += str(current.val)
                current = current.next
            
            return num
        
        def r_n(num_s):
            num_s.split()
            return ''.join(num_s[::-1])
        
        num1 = int(r_n(get_num(l1)))
        num2 = int(r_n(get_num(l2)))

        sum = num1+ num2
        rev_sum = str(sum)[::-1]

        l3 = ListNode()
        current = l3

        for i, num in enumerate(rev_sum):
            current.val = int(num)
            if i < len(rev_sum)-1:
                current.next = ListNode()
                current = current.next
        
        return l3
    
    
"""
OPTIMAL SOLUTION
"""

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

        dummy = ListNode(0) 
        current = dummy
        carry = 0

    
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


        

               