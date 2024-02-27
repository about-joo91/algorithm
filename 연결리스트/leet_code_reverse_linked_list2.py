class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and left == right:
            return head
        
        dummy = ListNode(0, head)
        left_node = dummy

        for _ in range(left - 1):
            left_node = left_node.next

        cur_node = left_node.next
        for _ in range(right - left):
            next_node = cur_node.next
            cur_node.next, next_node.next, left_node.next = next_node.next, left_node.next, next_node
            
        return dummy.next
