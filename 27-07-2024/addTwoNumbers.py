class Solution(object):
    def addTwoNumbers(self, l1, l2) :
        newNode = ListNode()
        current=newNode
        carry=0
        while l1 or l2 or carry:
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            total=l1val+l2val+carry
            carry =total//10
            current.next = ListNode(total % 10)
            current =current.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return newNode.next
