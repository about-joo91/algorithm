class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_map = {}
        result = Node(0)
        
        curr = head
        copy = result
        while curr:
            copy.next = Node(curr.val)
            list_map[curr] = copy.next
            curr, copy = curr.next, copy.next
        
        curr = head
        copy = result.next
        while curr:
            if curr.random:
                copy.random = list_map[curr.random]
            curr, copy = curr.next, copy.next

        return result.next
