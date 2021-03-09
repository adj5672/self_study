def Backtrack(idx):

    # 전역변수 불러오기
    global count
    global  min_value

    # 만약 마지막 행이면 최종 합을 최솟값을 비교하고 최솟값 갱신
    if idx == N:
        if count < min_value:
            min_value = count
            return
    # 마지막 행이 아니라면
    else:
        # 각 열 (index : i) 마다
        for i in range(N):
            # 해당 열이 사용이 되지 않았다면
            if visited[i] != 1:
                # 해당 열 사용처리
                visited[i] = 1
                # 해당 칸 값에 더하고
                count += arr[idx][i]
                # 만약 합이 이미 최솟값을 넘어섰다면 재귀를 진행하지 않는다.
                if count > min_value:
                    visited[i] = 0
                    count -= arr[idx][i]
                # 아직 최솟값을 넘지 않았다면
                else:
                    # 다음 행에 대해서 재귀를 진행한다.
                    Backtrack(idx+1)
                    # 재귀가 끝나면 방문처리와 합을 초기화 한다.
                    visited[i] = 0
                    count -= arr[idx][i]

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # N * N 행렬
    N = int(input())

    # 배열
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    
    # 기본 최솟값 설정
    min_value = 0
    for i in range(N):
        min_value += arr[i][i]

    # 재귀함수 실행
    visited = [0 for _ in range(N)]
    count = 0
    Backtrack(0)

    # 출력
    print('#{} {}'.format(test_case, min_value))