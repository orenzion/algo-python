class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def insert(node, val):
    if node == None:
        return Node(val)

    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    return node


def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current


def maxValueNode(node):
    current = node
    while current.left != None:
        current = current.right
    return current


def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.key)
        inorder(node.right)


def deleteNode(root, key):
    # base case
    if root is None:
        return None

    # if the key to be deleted is smaller then the node's value
    # then it lies in the left part of the tree
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        # the key lies in the right part of the tree
        root.right = deleteNode(root.right, key)
    # if the key is the same as in the note's value
    else:
        # Node with only one child or with no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children
        # get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root
