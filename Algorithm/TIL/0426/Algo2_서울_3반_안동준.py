# arr : 탐색 배열, target : 찾을 숫자, count : 탐색 횟수
# l : 탐색 구간 시작 인덱스, r : 끝 인덱스
def binary_search(arr, target, count, l, r):
    
    # 탐색에 실패한 경우
    if l > r:
        return [1000000, 1025]

    m = (l + r) // 2
    # 탐색 성공
    if target == arr[m]:
        return [target, count+1]
    # 왼쪽 탐색
    if target < arr[m]:
        return binary_search(arr, target, count+1, l, m-1)
    # 오른쪽 탐색
    else:
        return binary_search(arr, target, count+1, m+1, r)

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # N : 숫자 목록의 길이, M : 탐색 횟수를 비교할 숫자의 개수
    N, M = map(int,input().split())

    # targets : M 개의 탐색할 숫자들
    targets = list(map(int,input().split()))

    # arr : 정렬된 N개의 정수
    arr = list(map(int,input().split()))

    # result : (해당 숫자, 최소 탐색 횟수)
    result = [1000000, 1025]
    for t in targets:
        # sub_result : 이진 탐색 결과
        sub_result = binary_search(arr, t, 0, 0, N-1)
        # 최소 탐색 횟수 갱신
        if sub_result[1] < result[1]:
            result[0], result[1] = sub_result[0], sub_result[1]
        # 최소 탐색 횟수와 같을 경우 해당 숫자 비교
        elif sub_result[1] == result[1] and sub_result[0] < result[0]:
            result[0] = sub_result[0]

    # 출력
    print('#{} {} {}'.format(test_case, result[0], result[1]))