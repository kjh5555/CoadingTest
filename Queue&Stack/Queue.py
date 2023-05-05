from collections import deque

queue = deque()

#enque() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
#deque() 0(1)
queue.popleft()
queue.popleft()
queue.popleft()