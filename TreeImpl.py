
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