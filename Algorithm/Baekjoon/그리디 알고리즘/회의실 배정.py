# 회의 갯수
N = int(input())

confs = [list(map(int,input().split())) for _ in range(N)]

count = 0
while confs:
    room, stack = [], []
    room.append(confs.pop(0))
    for _ in range(len(confs)):
        cur = confs.pop(0)
        for conf in room:
            if not (cur[0] >= conf[1] or cur[1] <= conf[0]):
                stack.append(cur)
                break
        else:
            room.append(cur)
    print(room)
    print(stack)
    count += 1
    confs = stack

print(count) 