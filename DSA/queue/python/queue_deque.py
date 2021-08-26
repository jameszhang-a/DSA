from collections import deque

# Implementing a queue with default deque
# First In First Out

queue = deque()

# Add to right
queue.append("first")
queue.append("second")
queue.append("third")
print(queue)
# ['first', 'second', 'third']


queue.popleft()  # first
queue.popleft()  # second
print(queue)
# ['third']


############################################
one = deque(["in"])
print(one)


############################################
# empty deque is falsy

empty = deque()

if empty:
    print("empty is true")
else:
    print("empty is false")

empty.append(5)

if empty:
    print("filled is true")
else:
    print("filled is false")
