# 회문 확인용 함수 만들기 (회문이면 1 return, 아니면 0 return)
def palindrome(word):
    n = len(word) // 2
    for i in range(n):
        if word[i] != word[-i-1]:
            return 0
    else:
        return 1

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    N, M = map(int,input().split())
    result = []

    # 글자판 만들기
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    # 행방향 회문 확인하기
    for row in arr:
        if result:
            break
        for i in range(N-M+1):
            word = row[i:i+M]
            if palindrome(word):
                result = word
                break
                
    # 글자판 transpose
    for i in range(N):
        for j in range(N):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 열방향 회문 확인하기
    for col in arr:
        if result:
            break
        for i in range(N-M+1):
            word = col[i:i+M]
            if palindrome(word):
                result = word
                break

    # 출력
    print('#{} {}'.format(test_case,''.join(result)))