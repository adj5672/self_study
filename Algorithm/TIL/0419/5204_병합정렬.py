# 병합정렬
def merge_sort(arr):
    global count

    # N : 배열의 크기
    n = len(arr)
    # 배열의 크기가 1이면 그대로 배열 return
    if n <= 1:
        return arr

    # left_arr : 분할 후 왼쪽 배열, right_arr : 분할 후 오른쪽 배열
    # result_arr : 정렬된 배열
    left_arr = merge_sort(arr[0:n // 2])
    right_arr = merge_sort(arr[n // 2:n])
    result_arr = []

    # 오른쪽 마지막 원소가 더 작은 경우
    if left_arr[-1] > right_arr[-1]:
        count += 1

    left, right = 0, 0
    # 두 분할 배열이 모두 존재한다면 첫 번째 원소 비교 후 result_arr 에 append
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] >= right_arr[right]:
            result_arr.append(right_arr[right])
            right += 1
        else:
            result_arr.append(left_arr[left])
            left += 1
    # 좌측 배열만 존재한다면
    if right == len(right_arr):
        result_arr.extend(left_arr[left:])
    # 우측 배열만 존재한다면
    elif left == len(left_arr):
        result_arr.extend(right_arr[right:])

    # 정렬된 배열 return
    return result_arr


# test_case 갯수
T = int(input())

for test_case in range(1, T + 1):
    # N : 정수의 갯수, data : N개의 정수
    N = int(input())
    data = list(map(int, input().split()))

    # count : 오른쪽 원소가 먼저 복사되는 경우의 수
    count = 0

    # result : 정렬된 배열
    result = merge_sort(data)

    # 출력
    print('#{} {} {}'.format(test_case, result[N // 2], count))