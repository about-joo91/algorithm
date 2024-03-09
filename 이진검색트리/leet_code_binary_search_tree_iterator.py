class BSTIterator:
    head = TreeNode(0)
    cur_pointer = head

    def __init__(self, root: Optional[TreeNode]):
        self.orderTree(root)
        self.cur_pointer = self.head
    
    def orderTree(self, root: Optional[TreeNode]) -> None:
        if root:
            self.orderTree(root.left)
            cur_node = TreeNode(root.val)
            self.cur_pointer.right = cur_node
            self.cur_pointer = self.cur_pointer.right
            self.orderTree(root.right)


    def next(self) -> int:
        if self.cur_pointer.right:
            result = self.cur_pointer.right.val
            self.cur_pointer = self.cur_pointer.right
            return result
        return -1
        

    def hasNext(self) -> bool:
        return self.cur_pointer.right is not None


class BSTIterator:
    head = TreeNode(0)
    stack = []

    def __init__(self, root: Optional[TreeNode]):
        self.orderTree(root)
    
    def orderTree(self, root: Optional[TreeNode]) -> None:
        if root:
            self.orderTree(root.right)
            self.stack.append(root.val)
            self.orderTree(root.left)


    def next(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
