# test_case 갯수
T = int(input())

h = '0123456789ABCDEF'

# 16진수 -> 2진수
def binary(x):
    num = h.find(x)
    result = ''
    for i in range(3, -1, -1):
        if num & (1 << i):
            result += '1'
        else:
            result += '0'
    return result

# 2진수 -> 10진수
def decoding(code, ratio):
    result = ''
    for i in range(0, 56 * ratio, ratio * 7):
        sub_code = code[i:i + ratio * 7]
        if sub_code == '0' * 3 * ratio + '1' * 2 * ratio + '0' * 1 * ratio + '1' * 1 * ratio:
            result += '0'
        elif sub_code == '0' * 2 * ratio + '1' * 2 * ratio + '0' * 2 * ratio + '1' * 1 * ratio:
            result += '1'
        elif sub_code == '0' * 2 * ratio + '1' * 1 * ratio + '0' * 2 * ratio + '1' * 2 * ratio:
            result += '2'
        elif sub_code == '0' * 1 * ratio + '1' * 4 * ratio + '0' * 1 * ratio + '1' * 1 * ratio:
            result += '3'
        elif sub_code == '0' * 1 * ratio + '1' * 1 * ratio + '0' * 3 * ratio + '1' * 2 * ratio:
            result += '4'
        elif sub_code == '0' * 1 * ratio + '1' * 2 * ratio + '0' * 3 * ratio + '1' * 1 * ratio:
            result += '5'
        elif sub_code == '0' * 1 * ratio + '1' * 1 * ratio + '0' * 1 * ratio + '1' * 4 * ratio:
            result += '6'
        elif sub_code == '0' * 1 * ratio + '1' * 3 * ratio + '0' * 1 * ratio + '1' * 2 * ratio:
            result += '7'
        elif sub_code == '0' * 1 * ratio + '1' * 2 * ratio + '0' * 1 * ratio + '1' * 3 * ratio:
            result += '8'
        elif sub_code == '0' * 3 * ratio + '1' * 1 * ratio + '0' * 1 * ratio + '1' * 2 * ratio:
            result += '9'
    return result

for test_case in range(1,T+1):
    # N : 세로 크기, M : 가로 크기
    N, M = map(int,input().split())

    # 코드 배열 정보
    # code_row : 암호코드가 담겨있는 행, codes : 복호화한 코드들, result : 출력할 결과값
    arr = [list(input()[:M]) for _ in range(N)]
    code_row = []
    codes = []
    result = 0

    # 암호코드가 담겨있는 행 찾아내기
    for row in arr:
        if row != ['0'] * M:
            if row not in code_row:
                code_row.append(row)

    # 코드가 담겨있는 행 전체를 2진수로 변환하기
    binary_code = []
    for row in code_row:
        code = []
        for c in row:
            code.extend(list(binary(c)))
        binary_code.append(code)

    # 2진수 코드를 뒤에서부터 탐색하여 1을 찾는다.
    for row in binary_code:
        for idx in range(-1, -len(row)-1, -1):
            # 암호코드의 마지막 위치를 발견한 경우
            if row[idx] == '1':
                # 해당 암호코드의 비율 찾기, count : 암호 1개의 2진 자릿수
                now = '1'
                count = 1
                change = 0
                while change < 4:
                    if row[idx-count] == now:
                        count += 1
                    else:
                        now = row[idx-count]
                        count += 1
                        change += 1
                count -= 1
                # ratio : 너비 비율, n : 암호 길이, code : 암호코드(2진수)
                ratio = count // 7
                n = ratio * 56
                code = ''.join(row[idx-n+1:idx+1])
                # 암호코드 부분 초기화
                for i in range(n):
                    row[idx-i] = '0'
                # 2진 코드 복호화
                decode = decoding(code, ratio)
                if decode not in codes:
                    codes.append(decode)

    # 복호화한 각 코드들의 유효성 검사
    for code in codes:
        check = 0
        for idx, num in enumerate(code):
            if idx % 2:
                check += int(num)
            else:
                check += 3 * int(num)
        if not check % 10:
            for num in code:
                result += int(num)

    # 출력
    print('#{} {}'.format(test_case, result))