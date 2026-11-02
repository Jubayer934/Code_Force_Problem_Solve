from collections import deque

q = deque()
q.append(1)           # add to the right
q.append(2)
q.append(3)
print(q)              # deque([1, 2, 3])

print(q.popleft())    # 1  (remove from the left, first in, first out)
print(q)              # deque([2, 3])

print(q.pop())        # 3  (remove from the right, last in, first out)
print(q)              # deque([2])

q.appendleft(0)       # add to the left
print(q)              # deque([0, 2, 3])

q.append(4)
print(q)              # deque([0, 2, 3, 4])