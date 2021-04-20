def binary_search(arr, left, right, target):
    
    # direction : 0 ~ 중앙, -1 ~ 왼쪽 탐색, 1 ~ 오른쪽 탐색
    global direction

    # 탐색이 끝난 경우
    if left > right:
        return False

    middle = (left + right) // 2

    # 중앙 탐색
    if arr[middle] == target:
        return True
    # 왼쪽 탐색
    elif arr[middle] > target:
        if direction >= 0:
            direction = -1
            return binary_search(arr, left, middle-1, target)
        else:
            return False
    # 오른쪽 탐색
    else:
        if direction <= 0:
            direction = 1
            return binary_search(arr, middle+1, right, target)
        else:
            return False

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # N : A에 속한 정수의 갯수, M : B에 속한 정수의 갯수
    N, M = map(int,input().split())

    # A : 정렬된 배열, B : 탐색해야 할 정수들, count : 탐색 성공한 정수 갯수
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    count = 0
    
    # 각 숫자마다 이진탐색 실행
    for num in B:
        direction = 0
        if binary_search(A, 0, N-1, num):
            count += 1

    # 출력
    print('#{} {}'.format(test_case, count))

