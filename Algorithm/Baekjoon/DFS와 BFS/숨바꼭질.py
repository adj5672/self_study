from collections import deque

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
visited[N] = 1

queue = deque([N])
while not visited[K] and queue:
    cur = queue.popleft()
    if 0 <= 2 * cur < 100001 and not visited[2 * cur]:
        queue.append(2 * cur)
        visited[2 * cur] = visited[cur] + 1
    if cur > 0 and not visited[cur - 1]:
        queue.append(cur - 1)
        visited[cur - 1] = visited[cur] + 1
    if cur < 100000 and not visited[cur + 1]:
        queue.append(cur + 1)
        visited[cur + 1] = visited[cur] + 1

print(visited[K] - 1)