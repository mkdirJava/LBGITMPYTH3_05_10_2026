from collections import deque

tail = deque(open('error.log'), maxlen=10)
count = 0
while len(tail) > 0:
    if count % 2 == 0:
        print(tail.popleft())
    else:
        print(tail.pop()) # pop right
    count += 1
