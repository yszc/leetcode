# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        p1 = p.next
        p_1 = None
        res = None
        ppHead = None
        while True:
            pHead = p
            for i in range(k):
                p.next = p_1
                p_1 = p
                p = p1
                if p1 != None:
                    p1 = p1.next
                if p == None:
                    break
            if i != k-1:
                p = p_1
                p1 = p.next
                p_1 = None
                while i>=0:
                    p.next = p_1
                    p_1 = p
                    p = p1
                    if p1 != None:
                        p1 = p1.next
                    i -= 1

            if ppHead != None:
                ppHead.next = p_1
                if i < 0:
                    break
            ppHead = pHead
            if res == None:
                res = p_1
            if p == None:
                pHead.next = None
                break

        return res

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
            
print(Solution().reverseKGroup(head, 1))