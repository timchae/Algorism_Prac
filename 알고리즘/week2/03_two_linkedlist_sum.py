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


def get_linked_list_sum(linked_list_1, linked_list_2):

    
    aa = 0
    l11 = 0
    l12 = 0
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    sum1 = 0
    while cur1 is not None:
        if aa == 0:
            
            sum1 +=  (cur1.data + cur2.data)*100
        elif aa == 1:
            sum1 +=  (cur1.data + cur2.data)*10
        elif aa == 2:
            sum1 +=  cur1.data + cur2.data
        aa += 1
        cur1 = cur1.next
        cur2 = cur2.next

    # 구현해보세요!
    return sum1


linked_list_1 = LinkedList(7)
linked_list_1.append(7)
linked_list_1.append(9)

linked_list_2 = LinkedList(3)
linked_list_2.append(4)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))


# 간결성 그리고 100의자리 출력 방법
# def get_linked_list_sum(linked_list_1, linked_list_2):  
#     sum_1 = _get_linked_list_sum(linked_list_1)
#     sum_2 = _get_linked_list_sum(linked_list_2)

#     return sum_1 + sum_2


# def _get_linked_list_sum(linked_list):
#     sum = 0
#     head = linked_list.head
#     while head is not None:
#         sum = sum * 10 + head.data
#         head = head.next
#     return sum