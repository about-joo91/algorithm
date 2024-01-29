class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head and head.next:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        
        return False
