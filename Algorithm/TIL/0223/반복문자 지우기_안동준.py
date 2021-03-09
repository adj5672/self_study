# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 단어 받아오기
    words = list(input())
    # stack 생성
    stack = []
    
    # 주어진 문자열을 한개씩 차례로 받아오기
    for i in range(len(words)):
        # 만약 stack이 비어있으면 append
        if not stack:
            stack.append(words[i])
        # 만약 연속된 문자면 stack에서 pop
        elif words[i] == stack[-1]:
            stack.pop()
        # 연속된 문자가 아니면 stack에 append
        else:
            stack.append(words[i])

    # 순회 후 남은 문자열 길이 출력
    print('#{} {}'.format(test_case,len(stack)))