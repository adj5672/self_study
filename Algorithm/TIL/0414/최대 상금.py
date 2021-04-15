# test_case 갯수
T = int(input())

# 자리를 바꿀 두 숫자의 index 찾기 (6 C 2)
idxs = list(range(6))
combination = []
combinations = []

# 조합 함수
def comb(idx, remain, n):

    if remain == 0:
        result = [combination[i] for i in range(2)]
        combinations.append(result)
        return

    if n - idx < remain:
        return
    
    # idx를 선택한 경우
    combination.append(idxs[idx])
    comb(idx+1, remain-1, 6)
    combination.pop()
    # idx를 선택하지 않은 경우
    comb(idx+1, remain, 6)

# 함수실행
comb(0, 2, 6)

# C번 교환 후 가능한 상금의 경우
def change(num, remain):

    r_num = int(''.join(num))

    if remain == 0:
        if r_num not in visited:
            visited.append(r_num)
        return

    # ???
    if (r_num in visited) and remain > len(num) // 2:
        return

    for comb in tc_comb:
        idx1, idx2 = comb[0], comb[1]
        num[idx1], num[idx2] = num[idx2], num[idx1]
        change(num, remain-1)
        num[idx1], num[idx2] = num[idx2], num[idx1]

for test_case in range(1,T+1):
    # data : 숫자판, C : 교환 횟수, n : 자릿수
    data, C = input().split()
    data = list(data)
    C = int(C)
    n = len(data)

    # 가능한 index 조합 불러오기
    tc_comb = [c for c in combinations if c[0] < n and c[1] < n]

    # 교환 횟수가 0이 될 떄까지 교환해보기
    visited = []
    change(data, C)

    # 출력
    print('#{} {}'.format(test_case, max(visited)))