stack = list(range(10))
stack.append(10)
stack.pop()

from collections import deque
queue = deque(range(10))
queue.appendleft(-1)
queue.popleft()
queue.popleft()
