import Tree

def preOrder(root):
    if root is None:
        return
    data_list = []
    def preOrderhelper(root):
        if root is None:
            return
        data_list.append(root.data)
        preOrderhelper(root.left)
        preOrderhelper(root.right)

    preOrderhelper(root)
    return data_list

def postOrder(root):
    if root is None:
        return
    data_list = []
    def postOrderhelper(root):
        if root is None:
            return
        postOrderhelper(root.left)
        postOrderhelper(root.right)
        data_list.append(root.data)

    postOrderhelper(root)
    return data_list

def inOrder(root):
    if root is None:
        return
    data_list = []
    def inOrderhelper(root):
        if root is None:
            return
        inOrderhelper(root.left)
        data_list.append(root.data)
        inOrderhelper(root.right)

    inOrderhelper(root)
    return data_list

def getHeight(root):
    if root is None:
        return -1
    else:
        return max(getHeight(root.left), getHeight(root.right)) + 1

def LevelOrder(root):
    result = []
    if root is None:
        return result
    result.append(root.data)
    def LevelOrderHelper(root):
        # if root is None:
        #     return
        root.left and result.append(root.left.data)
        root.right and result.append(root.right.data)
        root.left and LevelOrderHelper(root.left)
        root.right and LevelOrderHelper(root.right)
    LevelOrderHelper(root)
    return result

def BST_Insert(root, value):
    if root is None:
        return Tree.TreeNode(data=value)
    if value < root.data:
        if root.left is None:
            root.left = Tree.TreeNode(data=value)
        else:
            BST_Insert(root.left, value)
    else:
        if root.right is None:
            root.right = Tree.TreeNode(data=value)
        else:
            BST_Insert(root.right, value)
    return root