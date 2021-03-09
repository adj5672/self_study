# 선형 큐

# 배열 사용
n = 5
queue = [0] * n
f, r = -1, -1

def isEmpty():
    return f == r

def isFull():
    return r == n-1

def enQueue(x):
    global r

    if isFull():
        print('Queue is full')
    else:
        r += 1
        queue[r] = x

def deQueue(x):
    global f

    if isEmpty():
        print('Queue is empty')
    else:
        f += 1
        return queue[f]

# 데이터 큐 삽입
for i in range(1,n+1):
    enQueue(i)
# 데이터 큐 출력
for i in range(1,n+1):
    print(deQueue(i))
    
# 리스트 사용
n = 5
queue = []

# 데이터 큐 삽입
for i in range(1,n+1):
    queue.append(i)
# 데이터 큐 출력
for i in range(1,n+1):
    print(queue.pop(0))