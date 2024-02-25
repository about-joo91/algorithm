class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        weight = 0
        head = ListNode()
        result = head
        while l1 or l2 or weight:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            cur_sum = l1_val + l2_val + weight
            cur_num = cur_sum % 10
            weight = cur_sum // 10

            result.next = ListNode(val=cur_num, next=None)
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
