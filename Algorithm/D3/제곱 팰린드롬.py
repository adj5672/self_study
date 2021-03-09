# 회문 확인 함수
def palindrom(n):
    for i in range(len(str(n))//2):
        if str(n)[i] != str(n)[-i-1]:
            return False
    else:
        return True

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    # 시작과 끝 숫자
    A, B = map(int,input().split())
    nums = list(range(A,B+1))
    # count 배열
    square = [0 for _ in range(len(nums))]

    for idx, num in enumerate(nums):
        # 제곱근이 정수고 num이 회문이고, 제곱근도 회문이면
        if num ** 0.5 == int(num ** 0.5) and palindrom(num) and palindrom(int(num ** 0.5)):
            # count
            square[idx] = 1
            
    # 출력
    print('#{} {}'.format(test_case,square.count(1)))