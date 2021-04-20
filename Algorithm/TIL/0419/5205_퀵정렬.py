# Lomuto (arr : 배열, p : partition 시작 인덱스, r : 피봇 인덱스, partition 마지막 인덱스)
def Lomuto(arr, p, r):
    # partition 의 크기가 1 이하인 경우
    if p >= r:
        return

    # x : 피봇
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    # 피봇의 좌측 partition 정렬
    Lomuto(arr, p, i)
    # 피봇의 우측 partition 정렬
    Lomuto(arr, i + 1, r)


# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 정수의 갯수, data : N개의 정수
    N = int(input())
    data = list(map(int, input().split()))

    Lomuto(data, 0, N-1)

    # 출력
    print('#{} {}'.format(test_case, data[N//2]))