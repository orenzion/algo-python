from BST2 import Node

if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = Node()
    for num in nums:
        bst.insert(num)

    print(type(bst))
    '''
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")

    print("4 exists:")
    print(bst.exists(4))
    print("2 exists:")
    print(bst.exists(2))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))
    '''
