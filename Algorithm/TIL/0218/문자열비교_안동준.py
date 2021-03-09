# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 단어 2개 받아오기
    word1 = input()
    word2 = input()

    # 만약 word1이 word2에 있으면 결과값 1로 저장
    result = 0
    if word1 in word2:
        result = 1

    # 출력
    print('#{} {}'.format(test_case,result))