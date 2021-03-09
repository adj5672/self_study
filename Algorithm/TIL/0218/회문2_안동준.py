# 회문 확인용 함수 만들기 (회문이면 1 return, 아니면 0 return)
def palindrome(word):
    n = len(word) // 2
    for i in range(n):
        if word[i] != word[-i-1]:
            return 0
    else:
        return 1

# 10개의 test_case
for _ in range(10):

    test_case = int(input())
    max_len = 0

    # 글자판 만들기
    arr = []
    for _ in range(100):
        arr.append(list(input()))

    # 행방향 회문 확인하기
    for M in range(1,101):
        for row in arr:
            for i in range(101-M):
                word = row[i:i+M]
                if len(word) > max_len and palindrome(word):
                    max_len = len(word)

    # 글자판 transpose
    for i in range(100):
        for j in range(100):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 열방향 회문 확인하기
    for M in range(1,101):
        for col in arr:
            for i in range(101-M):
                word = col[i:i+M]
                if len(word) > max_len and palindrome(word):
                    max_len = len(word)

    # 출력
    print('#{} {}'.format(test_case,max_len))