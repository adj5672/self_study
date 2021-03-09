# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 코드 받아오기
    code = input()
    # stack
    stack, result = [], 1

    for word in code:
        # 만약 여는 괄호면 stack에 append
        if word == '(' or word == '{':
            stack.append(word)
        # 만약 닫는 소괄호이면
        elif word == ')':
            # stack의 마지막 요소가 여는 소괄호인지 확인 후 맞으면 pop, 아니면 result = 0
            try:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 0
                    break
            # stack이 []이면(닫는 괄호가 더 많은 경우, or 닫는 괄호가 먼저 나온 경우)
            # indexerror가 발생하므로 예외처리
            except:
                result = 0
                break
        # 만약 닫는 중괄호이면
        elif word == '}':
            # stack의 마지막 요소가 여는 소괄호인지 확인 후 맞으면 pop, 아니면 result = 0
            try:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    result = 0
                    break
            # stack이 []이면(닫는 괄호가 더 많은 경우, or 닫는 괄호가 먼저 나온 경우)
            # indexerror가 발생하므로 예외처리
            except:
                result = 0
                break

    # 순회 후 stack에 남아있는 괄호가 존재한다면 result = 0
    if stack:
        result = 0

    # 출력
    print('#{} {}'.format(test_case,result))
