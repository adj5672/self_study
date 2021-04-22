def BFS(N):

    queue = [N]
    i = -1

    while True:
        # pop 사용 시 시간초과
        i += 1
        num = queue[i]

        if 0 < num + 1 <= 1000000 and not visited[num + 1]:
            visited[num + 1] = visited[num] + 1
            if num + 1 == M:
                return visited[num + 1]
            queue.append(num + 1)

        if 0 < num * 2 <= 1000000 and not visited[num * 2]:
            visited[num * 2] = visited[num] + 1
            if num * 2 == M:
                return visited[num * 2]
            queue.append(num * 2)

        if 0 < num - 1 <= 1000000 and not visited[num - 1]:
            visited[num - 1] = visited[num] + 1
            if num - 1 == M:
                return visited[num - 1]
            queue.append(num - 1)

        if 0 < num - 10 <= 1000000 and not visited[num - 10]:
            visited[num - 10] = visited[num] + 1
            if num - 10 == M:
                return visited[num - 10]
            queue.append(num - 10)

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # N : 시작 자연수, M : 만들 자연수
    N, M = map(int,input().split())

    # 방문 배열 (연산 횟수)
    visited = [0] * 1000001

    # 결과값
    result = BFS(N)

    # 출력
    print('#{} {}'.format(test_case, result))