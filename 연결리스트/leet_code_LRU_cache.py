class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class LRUCache:
    _capacity = 0
    _data = None
    _head = None
    _tail = None

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._data = {}
        self._head = ListNode(0, 0)
        self._tail = ListNode(0, 0)
        self._head.next = self._tail
        self._tail.prev =  self._head

    def get(self, key: int) -> int:
        if key in self._data:
            cur_node = self._data[key]
            cur_node.remove()
            self.insert_node_to_head(cur_node)
            return cur_node.val
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self._data:
            cur_node = self._data[key]
            cur_node.remove()
            self.insert_node_to_head(cur_node)
            cur_node.val = value
        else:
            if len(self._data) >= self._capacity:
                tail_node = self._tail.prev
                tail_node.remove()
                del self._data[tail_node.key]
            
            newNode = ListNode(key, value)
            self._data[key] = newNode
            self.insert_node_to_head(newNode)
    
    def insert_node_to_head(self, node):
        head_next = self._head.next
        self._head.next = node
        node.next = head_next
        node.prev = self._head
        head_next.prev = node
