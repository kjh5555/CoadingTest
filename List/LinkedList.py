

"""
first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next=third
first.value=6
"""
class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
      # tail Ver
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
        else :
            self.tail.next = new_node
            self.tail = self.tail.next
        #하나가 배열에 추가 될때 맨 뒤로 테일을 하나씩 옮겨줌
        """ new_node = Node(value)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while(current.next):
                    current = current.next
                current.next = new_node """
        
       

    def get(self,idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
        #get메소드는 O(n)
    def insert(self, idx, value):
        new_node = Node(value)
        new_node.value = value
        current = self.head

        if idx == 0:
            self.head = new_node
            self.head.next = current
        else:
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove_at(self, idx):
        current = self.head

        if idx == 0 :
            self.head == current.next
        else:    
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next  










li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
print(li)




