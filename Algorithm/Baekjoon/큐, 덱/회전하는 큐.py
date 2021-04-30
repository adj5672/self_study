from collections import deque

def move_left():
    queue.append(queue.popleft())

def move_right():
    queue.appendleft(queue.pop())

N, M = map(int,input().split())

queue = deque(list(range(1,N+1)))
count = 0
data = deque(list(map(int,input().split())))

while data:
    target = data.popleft()
    idx = queue.index(target)

    if idx <= len(queue) // 2:
        while queue[0] != target:
            count += 1
            move_left()
    else:
        while queue[0] != target:
            count += 1
            move_right()

    queue.popleft()

print(count)