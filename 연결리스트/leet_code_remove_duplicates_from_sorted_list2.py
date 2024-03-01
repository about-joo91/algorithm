class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, next=head)
        cur = dummy.next
        prev = dummy
        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate = cur.val
                while cur.next and cur.next.val == duplicate:
                    cur = cur.next
                
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next
