# babygin 확인 함수
def babygin(arr):

    for i in range(10):
        # run 인 경우
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return True
        # triplet 인 경우
        if arr[i] == 3:
            return True

    return False

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    
    # cards : 12장의 카드
    cards = list(map(int,input().split()))

    # 각 플레이어가 뽑은 숫자(index)카드의 갯수(value)
    player1 = [0 for _ in range(12)]
    player2 = [0 for _ in range(12)]

    # result : 승부의 결과
    result = 0

    # 카드가 없어질때까지
    while cards:
        # player1 이 카드를 받고 babygin 인지 확인
        player1[cards.pop(0)] += 1
        if babygin(player1):
            result = 1
            break
        # player2 가 카드를 받고 babygin 인지 확인
        player2[cards.pop(0)] += 1
        if babygin(player2):
            result = 2
            break

    # 출력
    print('#{} {}'.format(test_case, result))