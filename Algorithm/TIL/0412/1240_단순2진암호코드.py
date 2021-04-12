# test_case 갯수
T = int(input())

# 암호키
key = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

for test_case in range(1,T+1):
    # N : 배열의 세로크기, M : 배열의 가로크기
    N, M = map(int,input().split())

    # 배열 정보
    arr = [input() for _ in range(N)]

    # 암호코드가 포함되어 있는 행 찾기
    for row in arr:
        if row != '0' * M:
            code = row
            break

    # 뒤에서부터 처음 1이 나오는 index 탐색
    for idx in range(-1,-M-1,-1):
        if code[idx] == '1':
            i = idx
            break

    # 56자리의 암호코드 slicing 및 복호화
    decode = ''
    key_code = code[i-55:i+1]
    for j in range(0, 56, 7):
        decode += key.get(key_code[j:j+7])

    # 암호 유효성 검사
    check = 0
    for idx, num in enumerate(decode):
        if not idx % 2:
            check += 3 * int(num)
        else:
            check += int(num)

    # 출력값 계산
    result = 0
    if not check % 10:
        for num in decode:
            result += int(num)

    # 출력
    print('#{} {}'.format(test_case, result))