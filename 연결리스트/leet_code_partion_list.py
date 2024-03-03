class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head, big_head = ListNode(0), ListNode(0)
        small_node, big_node = small_head, big_head

        while head:
            if head.val < x:
                small_node.next = head
                small_node = small_node.next
            else:
                big_node.next = head
                big_node = big_node.next
            head = head.next
        
        small_node.next = big_head.next
        big_node.next = None

        return small_head.next
        
