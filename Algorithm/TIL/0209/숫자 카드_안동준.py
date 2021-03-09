# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 카드 장수
    N = int(input())
    cards = input()
    # 각 숫자의 갯수가 들어갈 count list 생성
    count = [0] * 10
    # 각 숫자 갯수 count
    for card in cards:
        count[int(card)] += 1
    # 카드 갯수가 최대인 숫자(max_number)와 그 갯수(max_count) 찾기
    max_number, max_count = 0, 0
    for idx, num in enumerate(count):
        if num >= max_count:
            max_number = idx
            max_count = num
    # 출력
    print('#{} {} {}'.format(test_case,max_number,max_count))