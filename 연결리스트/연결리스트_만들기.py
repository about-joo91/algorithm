class Node():
    def __init__(self,value):
        self.next_node = None
        self.value = value
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            cur_node = self.head

            while cur_node.next_node:
                cur_node = cur_node.next_node

            cur_node.next_node = Node(value)
            
        self._print()
        
        
    def remove(self, value):
        prev_node = None
        cur_node = self.head
        
        while cur_node:
            if cur_node.value == value:
                prev_node.next_node = cur_node.next_node
                break
            prev_node = cur_node
            cur_node = cur_node.next_node
            
        self._print()
        
    def find(self, value):
        cur_node = self.head
        
        while cur_node:
            if cur_node.value == value:
                return cur_node
            
            cur_node = cur_node.next_node
        else: return None
            
    def _print(self):
        cur_node = self.head
        
        while cur_node:
            print(cur_node.value, end= " ")
            if cur_node.next_node:
                print("->", end= " ")
            cur_node = cur_node.next_node
        print()
        
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.remove(2)
find_two = linked_list.find(3)
if find_two: print(find_two.value)
else: print(find_two)