import unittest
import TreeImpl
import Tree

class TreeCase(unittest.TestCase):
    def setUp(self):
        self.noneNode = None
        self.SingleNode = Tree.TreeNode(data=1)

        self.head = Tree.TreeNode(data=3)
        self.head.left = Tree.TreeNode(data=5)
        self.head.right= Tree.TreeNode(data=2)
        self.head.left.left = Tree.TreeNode(data=1)
        self.head.left.right = Tree.TreeNode(data=4)
        self.head.right.left = Tree.TreeNode(data=6)

        self.BSTTree = Tree.TreeNode(data=4)
        self.BSTTree.left = Tree.TreeNode(data=2)
        self.BSTTree.right= Tree.TreeNode(data=7)
        self.BSTTree.left.left = Tree.TreeNode(data=1)
        self.BSTTree.left.right = Tree.TreeNode(data=3)


    def test_preOrder(self):
        order_list = TreeImpl.preOrder(self.noneNode)
        self.assertEqual(order_list, None)

        order_list = TreeImpl.preOrder(self.head)
        self.assertEqual(order_list, [3, 5, 1, 4, 2, 6])

    def test_postOrder(self):
        order_list = TreeImpl.postOrder(self.noneNode)
        self.assertEqual(order_list, None)

        order_list = TreeImpl.postOrder(self.head)
        self.assertEqual(order_list, [1, 4, 5, 6, 2, 3])

    def test_inOrder(self):
        order_list = TreeImpl.inOrder(self.noneNode)
        self.assertEqual(order_list, None)

        order_list = TreeImpl.inOrder(self.head)
        self.assertEqual(order_list, [1, 5, 4, 3, 6, 2])

    def test_getHeight(self):
        self.assertEqual(TreeImpl.getHeight(self.noneNode), -1)
        self.assertEqual(TreeImpl.getHeight(self.SingleNode), 0)
        self.assertEqual(TreeImpl.getHeight(self.head), 2)

    def test_LevelOrder(self):
        self.assertEqual(TreeImpl.LevelOrder(self.noneNode), [])
        self.assertEqual(TreeImpl.LevelOrder(self.SingleNode), [self.SingleNode.data])
        self.assertEqual(TreeImpl.LevelOrder(self.head), [3, 5, 2, 1, 4, 6])

    def test_BST_Insert(self):
        self.assertEqual(TreeImpl.LevelOrder(TreeImpl.BST_Insert(self.noneNode, 1)), [1])
        self.assertEqual(TreeImpl.inOrder(TreeImpl.BST_Insert(self.SingleNode, 0)), [0, 1])
        self.assertEqual(TreeImpl.inOrder(TreeImpl.BST_Insert(self.BSTTree, 6)), [1, 2, 3, 4, 6, 7])

if __name__ == '__main__':
    unittest.main()
