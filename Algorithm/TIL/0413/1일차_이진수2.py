# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 소수 받아오기
    num = float(input())

    result = ''
    # 소숫점 아래 12자리 까지 2진수 변환
    for i in range(-1,-13, -1):
        if num // 2 ** i:
            result += '1'
            num = num % 2 ** i
        else:
            result += '0'
        
        # 완전히 나누어 졌으면 for문 종료
        if num == 0:
            break

    # 만약에 13자리 이상 필요한 경우 overflow
    if num:
        result = 'overflow'

    # 출력
    print('#{} {}'.format(test_case,result))