class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        a = 0
        while cur is not None:
            if a == index:
                return cur
            a += 1
            cur = cur.next
        return "index 번째 노드를 반환해보세요!"

    def add_node (self, index, value):

        cur = self.head
        count = 0
        node = Node(value)

        if index == 0:
                node.next = cur 
                self.head = node
                return 

        while count < index:
                             
            if (index - 1) == count:
                
                n_copy = cur.next
                cur.next = node
                node.next = n_copy

            cur = cur.next
            count += 1
    def delete_node(self, index):

        node = self.get_node(index)

        if index == 0:
            self.head = self.get_node(1)
            return 

        self.get_node(index-1).next = node.next



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(1)
linked_list.append(8)
print(linked_list.head.data)
linked_list.add_node(4,3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()
 # -> 5를 들고 있는 노드를 반환해야 합니다!
