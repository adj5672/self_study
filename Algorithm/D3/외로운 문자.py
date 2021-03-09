# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    code = input()
    result = []
    # 각 알파벳마다
    for word in code:
        # result에 없으면 append
        if word not in result:
            result.append(word)
        # 있으면 remove
        elif word in result:
            result.remove(word)

    # 만약 남은 문자가 없으면 Good        
    if not result:
        answer = 'Good'
    # 있으면 오름차순 정렬
    else:
        result.sort()
        answer = ''.join(result)

    # 출력
    print('#{} {}'.format(test_case,answer))