class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        result = ListNode(0, next=head)
        
        end = head
        length = 1
        while end.next:
            end = end.next
            length+=1
        end.next = head

        cur = head
        k = length - (k % length) - 1
        while k > 0:
            cur = cur.next
            k-=1
        
        result.next = cur.next
        cur.next = None
        return result.next
        
