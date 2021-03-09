# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 후위 표기 코드 받아오기
    code = input().split()
    stack = []
    result = ''

    for c in code:

        # 숫자라면 stack에 쌓기
        try:
            stack.append(int(c))
        except:
            pass

        # + 연산
        if c == '+':
            try:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1)+int(n2))
            except:
                result = 'error'
                break
        
        # - 연산
        elif c == '-':
            try:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2)-int(n1))
            except:
                result = 'error'
                break

        # * 연산
        elif c == '*':
            try:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1)*int(n2))
            except:
                result = 'error'
                break

        # / 연산
        elif c == '/':
            try:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(int(n2)/int(n1)))
            except:
                result = 'error'
                break
        
        # 연산 종료
        elif c == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
    
    # 출력
    print('#{} {}'.format(test_case, result))