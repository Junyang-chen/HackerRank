import unittest
import LinkedList

class LinkedListFactary(unittest.TestCase):
    def test_empty_list(self):
        data_list = []
        singlelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.SINGLELINKEDLIST)
        self.assertEqual(singlelinkedlist, None)
        doublelinkedlist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        self.assertEqual(doublelinkedlist, None)

    def test_single_list(self):
        data_list = [1,2,3,4,5]
        singlelist = LinkedList.LinkedListFactary(data_list, LinkedList.SINGLELINKEDLIST)
        i = 0
        while(singlelist):
            self.assertEqual(singlelist.data, data_list[i])
            i += 1
            singlelist = singlelist.next

    def test_double_list(self):
        data_list = [1, 2, 3, 4, 5]
        singlelist = LinkedList.LinkedListFactary(data_list, LinkedList.DOUBLELINKEDLIST)
        i = 0
        while (singlelist.next):
            self.assertEqual(singlelist.data, data_list[i])
            i += 1
            singlelist = singlelist.next

        while (singlelist):
            self.assertEqual(singlelist.data, data_list[i])
            i -= 1
            singlelist = singlelist.prev

if __name__ == '__main__':
    unittest.main()
