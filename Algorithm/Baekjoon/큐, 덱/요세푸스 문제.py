from collections import deque

N, K = map(int,input().split())

result = []
people = deque(list(range(1,N+1)))
i = 0

while people:
    kill = []
    while True:
        i += K
        if i > len(people):
            i = (i % len(people)) - K
            break
        kill.append(people[i-1])
        result.append(people[i-1])
        if i == len(people):
            break
    for k in kill:
        people.remove(k)

print(result)