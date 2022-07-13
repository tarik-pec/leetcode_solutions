
#2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode(0)
        currNode = ansHead
        remainder = 0
        # if there is a remainder or digits in ints l1 or l2 to add, continue the sum.
        while remainder != 0 or l1 != None or l2 != None:
            # Take the values in the integers of l1 and l2, if we have 'gone through all the digits', set the value to 0.
            l1Value = l1.val if l1 else 0
            l2Value = l2.val if l2 else 0
            # Add the current digits and the remainder; add the first digit of this sum to the 'answer' linked list, and update the remainder
            curr_sum = l1Value + l2Value + remainder
            newNode = ListNode(curr_sum%10)
            remainder = curr_sum//10
            currNode.next = newNode
            currNode = newNode
            # Move onto the next nodes of l1 and l2, otherwise set them to None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ansHead.next
