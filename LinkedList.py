"""
This file is written by Junyang Chen for datastrucutures of Linked list
"""

class DoubleLinkedNode(object):
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return 'Node({0})'.format(self.data)

    def __str__(self):
        return 'Node({0})'.format(self.data)

class SingleLinkedNode(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node({0})'.format(self.data)

    def __str__(self):
        return 'Node({0})'.format(self.data)

SINGLELINKEDLIST = 0
DOUBLELINKEDLIST = 1

def LinkedListFactary(data_list, linkedlist_type):
    # function to create a linked list
    # params: data(list), type(Single, double)
    if not bool(data_list):
        return None
    if linkedlist_type == SINGLELINKEDLIST:
        head = SingleLinkedNode(data=data_list[0])
        curr = head
        for val in data_list[1:]:
            curr.next = SingleLinkedNode(data=val)
            curr = curr.next
    elif linkedlist_type == DOUBLELINKEDLIST:
        head = DoubleLinkedNode(data=data_list[0])
        curr = head
        for val in data_list[1:]:
            curr.next = DoubleLinkedNode(data=val, prev=curr)
            curr = curr.next
    return head