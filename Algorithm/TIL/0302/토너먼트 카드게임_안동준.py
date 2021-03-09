# 가위바위보 함수 (가위바위보에서 이긴 학생의 index를 return)
def RCP(x,y):
    # A : x번 학생의 카드, B : y번 학생의 카드
    A, B = card[x], card[y]
    if A == B:
        return x
    elif A == 1 and B == 2:
        return y
    elif A == 1 and B == 3:
        return x
    elif A == 2 and B == 1:
        return x
    elif A == 2 and B == 3:
        return y
    elif A == 3 and B == 1:
        return y
    elif A == 3 and B == 2:
        return x
    
# 분할 정복 재귀 함수
def tournament(list):
    # 만약 전체 길이가 1 이라면 부전승으로 학생의 index를 return
    if len(list) == 1:
        return list[0]
    # 만약 전체 길이가 2 라면 가위바위보를 이긴 학생의 index를 return
    elif len(list) == 2:
        return RCP(list[0],list[1])
    # 전체 길이가 2보다 크면 두 그룹으로 나눈다.
    else:
        return RCP(tournament(list[:len(list) // 2 + 1]), tournament(list[len(list) // 2 + 1:]))

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # 인원 수
    N = int(input())

    # 뽑은 카드
    card = list(map(int,input().split()))

    # 각 학생의 index (index = 학생번호 - 1)
    idx = [i for i in range(N)]

    # 우승한 학생의 학생번호
    winner = tournament(idx) + 1

    # 출력
    print('#{} {}'.format(test_case, winner))