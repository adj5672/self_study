# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    # 알파벳과 갯수
    data = []
    for _ in range(N):
        data.append(list(input().split()))
    
    # 알파벳 나열
    words = []
    for i in range(N):
        for j in range(int(data[i][1])):
            words.append(data[i][0])

    # 출력
    print('#{}'.format(test_case))
    for idx, word in enumerate(words):
        if idx % 10 == 9:
            print(word)
        else:
            print(word,end='')
    print('')
