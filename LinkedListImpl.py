import LinkedList

def ConvertlinkedListTolist(head):
    data_list = []
    while(head):
        data_list.append(head.data)
        head = head.next
    return data_list

def SortedInsert(head, data):
    # insert into doublely linked list
    if head is None:
        return LinkedList.DoubleLinkedNode(data=data)
    if data < head.data:
        new_head = LinkedList.DoubleLinkedNode(data=data, next=head)
        head.prev = new_head
        return new_head
    curr = head
    while (curr.next and curr.next.data < data):
        curr =  curr.next
    new_node = LinkedList.DoubleLinkedNode(data=data, prev=curr, next=curr.next)
    curr.next = new_node
    if curr.next is not None:
        curr.prev = new_node
    return head

def ReverseDoubleLinkedList(head):
    if head is None or head.next is None:
        return head
    curr = head
    next = head.next
    prev = curr.prev
    curr.prev = next
    curr.next = prev
    while(next):
        next.prev = next.next
        next.next = curr
        curr = curr.prev
        next = next.prev
    return curr