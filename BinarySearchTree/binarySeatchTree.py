class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None:
            self.val = val
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        return

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_min_value_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def get_max_value_node(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self

        if val < self.val:
            if self.left != None:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right != None:
                self.right.delete(val)
            return self

        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
