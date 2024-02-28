class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth_node = head
        for _ in range(n):
            nth_node = nth_node.next
        
        if not nth_node:
            return head.next

        cur_node = head
        while nth_node.next:
            cur_node = cur_node.next
            nth_node = nth_node.next

        cur_node.next = cur_node.next.next
        
        return head
