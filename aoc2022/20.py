
class Node:
    def __init__(self, val, prev=None, next= None):
        self.val = val
        self.ognext = next
        self.prev = prev
        self.next = next

    def setOGNext(self, next):
        self.ognext = next
        self.next = next
        
    def nextPosition(self):
        pointer = self
        if self.val > 0:
            for i in range(0,self.val):
                pointer = pointer.next
        if self.val < 0:
            for i in range(0,abs(self.val)+1):
                pointer = pointer.prev
        return pointer
    
    def __repr__(self):
        s = str(self.val)
        n = self.next
        while n != self:
            s += ', '+ str(n.val)
            n = n.next
        return s

def moveNodes(head):
    n = head
    while n is not None:
        v = n.val
        if v == 0:
            n=n.ognext
            continue
        toReplace = n.nextPosition()
        #print('moving', v, 'between', toReplace.val, 'and', toReplace.next.val)
        # patch old position
        n.prev.next = n.next
        n.next.prev = n.prev
        #change self pointers
        n.prev = toReplace
        n.next = toReplace.next
        #insert in new position
        n.prev.next = n
        n.next.prev = n
        n = n.ognext
    return head

def calcGrove(head):
    res = []
    n = head
    while n.val != 0:
        n = n.next
    head = n
    for _ in range(0,1000):
        n = n.next
    res.append(n.val)
    for _ in range(0,1000):
        n = n.next
    res.append(n.val)
    for _ in range(0,1000):
        n = n.next
    res.append(n.val)
    print(res)
    return sum(res)
        
def printCurrent(head):
    n = head
    print('\n\nVVV')
    print(n.val)
    n = head.next
    while n != head:
        print(n.val)
        n = n.next

with open("aoc2022/20.txt") as f:
    lines = [x.strip() for x in f]
    head = None
    tail = None
    prev = None
    for l in lines:
        node = Node(int(l), prev)
        if head is None:
            head = node
        if prev is not None:
            prev.setOGNext(node)
        prev = node
        tail = node
    
    #circular
    head.prev = tail
    tail.next = head
    
    head = moveNodes(head)
    while head.val != 5157:
        head = head.next
    print(head)
    print(calcGrove(head))
    
    
    # 8494 - too high
    # 0  1   2  3   4  5  6
    # 1, 2, -3, 3, -2, 0, 4