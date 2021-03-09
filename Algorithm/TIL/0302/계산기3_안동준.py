# test_case 의 갯수는 10개
for test_case in range(1,11):

    # test_case의 길이
    N = int(input())
    
    # code : 중위 표기식
    code = list(input())
    stack = []
    result = []
    
    # 후위 표기식 만들기
    # 코드의 각 문자열에 대해서
    for c in code:

        # 피연산자이면 result에 append
        try:
            result.append(int(c))
        except:
            pass

        # 여는 괄호이면 stack에 append
        if c == '(':
            stack.append(c)

        # + 연산자이면 여는 괄호가 나올 때 까지 stack에서 pop하여 result에 append
        elif c == '+':
            while stack:
                if stack[-1] == '(':
                    break
                result.append(stack.pop())
            stack.append(c)

        # * 연산자이면 여는 괄호가 나올 때 까지 또는 + 연산자가 나올때 까지
        # stack에서 pop하여 result에 append
        elif c == '*':
            while stack:
                if stack[-1] == '(' or stack[-1] == '+':
                    break
                result.append(stack.pop())
            stack.append(c)

        # 닫는 괄호이면 여는 괄호가 나올 때 까지 stack에서 pop하여 result에 append
        elif c == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

    # stack의 나머지 연산자들을 result에 append
    while stack:
        result.append(stack.pop())
    # 후위 표기식 완성

    ##################################################################################

    # 후위 표기식 계산
    for c in result:

        # 피연산자이면 stack에 append
        try:
            stack.append(int(c))
        except:
            pass

        # + 연산자이면 stack에서 두 숫자를 꺼내 계산 후 다시 stack에 append
        if c == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 + n2)

        # * 연산자이면 stack에서 두 숫자를 꺼내 계산 후 다시 stack에 append
        if c == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 * n2)

    # 최종 계산값 출력
    print('#{} {}'.format(test_case, stack[-1]))