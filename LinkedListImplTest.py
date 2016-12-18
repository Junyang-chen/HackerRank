import unittest
import LinkedListImpl
import LinkedList

class MyTestCase(unittest.TestCase):
    def test_ReverseDoubleLinkedList(self):
        # [1,2,3,4,5] should be  [5,4,3,2,1]
        data_list_all = []
        data_list_all.append(list(range(100)))
        data_list_all.append([1, 2, 3, 4, 5])
        data_list_all.append([])
        for data_list in data_list_all:
            doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
            doublelinkedlist = LinkedListImpl.ReverseDoubleLinkedList(doublelinkedlist)
            for val in reversed(data_list):
                self.assertEqual(doublelinkedlist.data, val)
                doublelinkedlist = doublelinkedlist.next

    def test_SortedInsert(self):
        data_list = []
        doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        data_list = LinkedListImpl.ConvertlinkedListTolist(LinkedListImpl.SortedInsert(doublelinkedlist, 1))
        self.assertEqual(data_list, [1])

        data_list =[1]
        doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        data_list = LinkedListImpl.ConvertlinkedListTolist(LinkedListImpl.SortedInsert(doublelinkedlist, 0))
        self.assertEqual(data_list, [0, 1])

        data_list =[1]
        doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        data_list = LinkedListImpl.ConvertlinkedListTolist(LinkedListImpl.SortedInsert(doublelinkedlist, 2))
        self.assertEqual(data_list, [1, 2])

        data_list = [1, 2, 4, 6, 8]
        doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        data_list = LinkedListImpl.ConvertlinkedListTolist(LinkedListImpl.SortedInsert(doublelinkedlist, 3))
        self.assertEqual(data_list, [1, 2, 3, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
