# baby-gin 확인 함수
def is_babygin():

    result = 0
    
    # count 배열을 두 번 순회
    for _ in range(2):
        for i in range(10):
            # triplet 인지 확인
            if count[i] >= 3:
                count[i] -= 3
                result += 1
            # run 인지 확인
            if count[i] and count[i+1] and count[i+2]:
                count[i] -= 1
                count[i+1] -= 1
                count[i+2] -= 1
                result += 1

    if result == 2:
        return True
    else:
        return False

# test_case 갯수
T = int(input())

for test_case in range(1, T+1):
    # num : 6자리 숫자, count : 각 숫자의 갯수 배열
    num = input()
    count = [0 for _ in range(12)]

    # 6자리 숫자에서 각 숫자의 갯수 count
    for n in num:
        count[int(n)] += 1

    # baby-gin 확인
    if is_babygin():
        result = 1
    else:
        result = 0

    # 출력
    print('#{} {}'.format(test_case, result))