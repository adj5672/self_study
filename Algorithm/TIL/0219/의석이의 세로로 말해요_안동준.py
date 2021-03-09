# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 단어장 만들기
    words = []
    for _ in range(5):
        words.append(list(input()))

    # 각 행 배열에 최대 index 구하기
    words_index = [-1 for _ in range(5)]
    for i in range(5):
        words_index[i] += len(words[i])

    # words_index 중 최댓값 구하기
    max_index = 0
    for idx in words_index:
        if idx > max_index:
            max_index = idx

    # 2차원 배열 순회하며 결과값 만들기
    result = []
    # i : 열 번호, j : 행 번호
    for i in range(max_index+1):
        for j in range(5):
            # 만약 j 행의 최대 index(열 번호 최댓값) 보다 열 번호가 크다면 글자가 없으므로 continue
            if words_index[j] < i:
                continue
            # 아니면 결과값에 append
            else:
                result.append(words[j][i])

    # 출력
    print('#{} {}'.format(test_case,''.join(result)))