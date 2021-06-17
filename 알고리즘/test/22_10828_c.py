



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):                 # 현재 [4] 밖에 없다면
        new_head = Node(value)             # [3] 을 만들고!
        new_head.next = self.head          # [3] -> [4] 로 만든다음에
        self.head = new_head  

    # pop 기능 구현
    def pop(self):
        if self.empty() == 1:                  # 만약 비어있다면 에러!
            return -1
        delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head.data

    def top(self):
        if self.empty() == 1:
            return -1

        return self.head.data

    # isEmpty 기능 구현
    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0
        
    
    def size(self):
        if self.empty() == 1:
            return 0
        a = self.head
        count = 1
        while a.next is not None:
            a = a.next
            count +=1
        return count

a = int(input())
bb = Stack()
d = []
for i in range(a):
    b = []
    b = list(input().split())
    
    
    
    if b[0] == 'push':
        c = bb.push(int(b[1]))
    elif b[0] == 'pop':
        c = bb.pop()
        d.append(c)

    elif b[0] == 'top':
        c = bb.top()
        d.append(c)
    elif b[0] == 'empty':
        c = bb.empty()
        d.append(c)
    elif b[0] == 'size':
        c = bb.size()
        d.append(c)

for i in d:
    print(i)
        