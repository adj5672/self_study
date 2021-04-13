# test_case 갯수
T = int(input())

h = '0123456789ABCDEF'

for test_case in range(1,T+1):
    # N : 자릿수, data : N자리 16진수
    N, data = input().split()
    
    # 2진수 표현
    bin_num = ''

    # 각 16진수 숫자마다
    for hex_num in data:
        # 10진수로 변환
        num = h.find(hex_num)
        # 비트 연산을 통해 2진수로 변환
        for i in range(3, -1, -1):
            if num & (1 << i):
                bin_num += '1'
            else:
                bin_num += '0'

    # 출력
    print('#{} {}'.format(test_case, bin_num))