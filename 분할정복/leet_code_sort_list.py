class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last_node = self.left_last_node(head)
        mid = last_node.next
        last_node.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def left_last_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        newHead = cur = ListNode()
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next= right
                right = right.next
            cur = cur.next
        
        cur.next = left or right

        return newHead.next
