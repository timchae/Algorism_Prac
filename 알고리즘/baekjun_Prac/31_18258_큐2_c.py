class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def push(self, value):              
        new_node = Node(value)             
        if self.empty():
            self.head = new_node           # head 에 new_node를
            self.tail = new_node   
            self.n += 1        # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node          
        self.tail = new_node		  
        self.n += 1

    def pop(self):
        if self.empty() == 1:
            return -1        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        self.n -= 1
        return delete_head.data    

    def front(self):
        if self.empty() == 1:
            return -1
    
        return self.head.data
    
    def back(self):
        if self.empty() == 1:
            return -1
    
        return self.tail.data

    def empty(self):
        if bool(self.head is None):
            return 1
        else:
            return 0
        

    def size(self):
        return self.n

a = int(input())
q = Queue()
res = []
for i in range(a):

    b = list(input().split())
    
    if b[0] == 'push':
        nn = int(b[1])
        q.push(nn)
    elif b[0] == 'pop':
               
        res.append(q.pop())
    elif b[0] == 'size':
        res.append(q.size())
    elif b[0] == 'empty':
        res.append(q.empty())
    elif b[0] == 'front':
        res.append(q.front())
    elif b[0] == 'back':
        res.append(q.back())
for i in res:
    print(i)