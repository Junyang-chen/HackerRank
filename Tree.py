"""
This file is written by Junyang Chen for datastrucutures of tree
"""

class TreeNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return 'Node({0})'.format(self.data)

    def __str__(self):
        return 'Node({0})'.format(self.data)