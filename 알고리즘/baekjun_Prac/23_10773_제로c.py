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
        
        delete_head = self.head.data              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head

 
        
a = int(input())
sum1 = 0
aa = Stack()
for i in range(a):

    num = int(input())
    
    
    if num != 0:
        aa.push(num)
        sum1 += num
    else:
        
        
        sum1 -= aa.pop()
        

print(sum1)
    
    