from collections import deque

# Using list
lst = list(range(100_000))
lst.pop()     

# Using deque
dq = deque(range(100_000))
dq.popleft()  

print("Queue operation completed")

