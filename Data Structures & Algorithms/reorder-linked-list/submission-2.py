# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #[0,1,2,3,4,5,6]
        #[0,1,2,3,6,5,4]
        #             v
        #[6,1,5,2,4,3]
        #       ^     
        if not head:
            return None
        
        #Step1: Reverse the second half of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondListHead = slow.next
        secondListPrev = None
        slow.next = None #Disconnect 
        while secondListHead:
            temp = secondListHead.next
            secondListHead.next = secondListPrev
            secondListPrev = secondListHead
            secondListHead = temp
      
    
        currentNode = head
        while secondListPrev:
            tempList1 = currentNode.next #this value is 4
            tempList2 = secondListPrev.next #this value is 6
            currentNode.next = secondListPrev
            secondListPrev.next = tempList1
            currentNode = tempList1
            secondListPrev = tempList2
        
    

