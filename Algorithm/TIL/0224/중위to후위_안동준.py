# (6+5*(2-8)/2)
# 6528-*2/+

# 피연산자인지 확인하는 함수
def is_number(x):
    if x not in operator and x not in braket:
        return True
    else:
        return False

infix = list(input())
stack, postfix = [], []
operator =["*","/","+","-"]
braket = ["(",")"]

# 각 토큰에 대해서
for token in infix:

    # 여는 괄호이면 stack에 append
    if token == braket[0]:
        stack.append(token)

    # 피연산자이면 postfix에 append
    elif is_number(token):
        postfix.append(token)

    # 곱하기 또는 나누기 연산자이면
    elif token == operator[0] or token == operator[1]:
        # token보다 우선순위가 같거나 높은 것들을 모두 pop하여 postfix에 append
        while stack[-1] == operator[0] or stack[-1] == operator[1]:
            postfix.append(stack.pop())
        # token을 stack에 append
        stack.append(token)

    # 더하기 또는 빼기 연산자이면
    elif token == operator[2] or token == operator[3]:
        # token보다 우선순위가 같거나 높은 것들을 모두 pop하여 postfix에 append
        while stack[-1] in operator:
            postfix.append(stack.pop())
        # token을 stack에 append
        stack.append(token)

    # 닫는 괄호이면
    elif token == braket[1]:
        # 여는괄호 전까지 stack의 top들을 pop하여 postfix에 append
        while stack[-1] != braket[0]:
            postfix.append(stack.pop())
        # stack에서 여는 괄호 pop
        stack.pop()

# 출력
print(''.join(postfix))