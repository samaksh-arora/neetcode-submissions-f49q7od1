# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return[]
        if not head.next:
            return None
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prevPointerOfSecondHalf = slow.next
        slow.next = None #list has been seperated

        #reverse the second list
        currPointerOfSecondHalf = prevPointerOfSecondHalf.next
        prevPointerOfSecondHalf.next = None
        while currPointerOfSecondHalf:
            temp = currPointerOfSecondHalf.next
            currPointerOfSecondHalf.next = prevPointerOfSecondHalf
            prevPointerOfSecondHalf = currPointerOfSecondHalf
            currPointerOfSecondHalf = temp
        secondHead = prevPointerOfSecondHalf

        curr1, curr2 = head, secondHead 

        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2
        

               
            

