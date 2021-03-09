# 피연산자인지 확인하는 함수
def is_number(x):
    if x not in operator:
        return True

for test_case in range(1,11):
    
    # test_case의 길이
    N = int(input())
    # infix : 중위 문자열을 받아옴, postfix : 변환 한 후위 문자열을 담을 배열
    infix = list(input())
    stack, postfix = [], []
    operator = ["*", "+"]

    # 후위 문자열로 전환
    for token in infix:
        # 피연산자이면 postfix에 append
        if is_number(token):
            postfix.append(token)
        # token이 곱하기 연산자라면
        elif token == operator[0]:
            # stack에 원래 채워져있던게 있다면 top 에서부터 차례로 '*'만을 pop해서 postfix에 append, 그 후 token을 stack에 append
            # stack이 비어있다면 바로 stack에 append
            while len(stack) != 0 and stack[-1] == operator[0]:
                postfix.append(stack.pop())
            stack.append(token)
        # token이 더하기 연산자라면
        elif token == operator[1]:
            # stack의 모든 operator를 pop해서 postfix에 append, 그 후 token을 stack에 append
            # stack이 비어있다면 바로 stack에 append
            while len(stack) != 0 and stack[-1] in operator:
                postfix.append(stack.pop())
            stack.append(token)

    # stack에 남은 연산자 모두 pop
    if stack:
        for _ in range(len(stack)):
            postfix.append(stack.pop())

    # 후위 표기식 계산
    for token in postfix:
        # 피연산자라면 stack에 append
        if is_number(token):
            stack.append(token)
        # 곱하기 연산자라면
        elif token == operator[0]:
            # stack에서 2개의 피연산자를 pop하여 계산 후 다시 stack에 append
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) * int(y)))
        # 더하기 연산자라면
        elif token == operator[1]:
            # stack에서 2개의 피연산자를 pop하여 계산 후 다시 stack에 append
            x = stack.pop()
            y = stack.pop()
            stack.append(str(int(x) + int(y)))

    # 계산 후 결과값 출력
    print('#{} {}'.format(test_case, stack[0]))