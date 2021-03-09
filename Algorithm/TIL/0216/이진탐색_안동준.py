# 이진탐색을 통해 start와 end 사이에서 key 값을 찾기까지 count를 구하는 함수
def binary_count(start, end, key):
    count = 0
    while start <= end:
        middle = (start + end) // 2
        # middle 과 key가 같다면 count값 반환
        if key == middle:
            count += 1
            return count
        # key 값이 middle보다 크다면 middle 우측탐색
        elif key > middle:
            start = middle
            count += 1
        # key 값이 middle보다 작다면 middle 좌측탐색
        else:
            end = middle
            count += 1
    # count값 반환
    return count

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    Page, Pa, Pb = map(int,input().split())
    # count_a : A가 Pa를 찾기까지 탐색횟수, count_b : B가 Pb를 찾기까지 탐색횟수
    count_a = binary_count(1, Page, Pa)
    count_b = binary_count(1, Page, Pb)

    # 출력
    if count_a < count_b:
        print('#{} A'.format(test_case))
    elif count_a > count_b:
        print('#{} B'.format(test_case))
    else:
        print('#{} 0'.format(test_case))

