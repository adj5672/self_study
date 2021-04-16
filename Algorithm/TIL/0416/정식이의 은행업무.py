# idx 번째 숫자를 바꿀 떄 가능한 송금액 (2진수)
def bin_cost(arr, idx):

    copy_arr = [x for x in arr]
    total = 0

    # idx 번째 숫자를 바꾼다.
    if arr[idx] == 0:
        copy_arr[idx] = 1
    else:
        copy_arr[idx] = 0
    
    # 2진수 계산
    for i in range(len(arr)):
        total += copy_arr[i] * (1 << (len(arr) - i - 1))
    
    # 가능 송금액에 추가
    case.append(total)

# idx 번째 숫자를 바꿀 떄 가능한 송금액 (3진수)
def ter_cost(arr, idx):

    global result

    copy_arr1, copy_arr2 = [x for x in arr], [x for x in arr]
    total1, total2 = 0, 0

    # idx 번째 숫자를 바꾼다.
    if arr[idx] == 0:
        copy_arr1[idx], copy_arr2[idx] = 1, 2
    elif arr[idx] == 1:
        copy_arr1[idx], copy_arr2[idx] = 0, 2
    else:
        copy_arr1[idx], copy_arr2[idx] = 0, 1
    
    # 3진수 계산
    for i in range(len(arr)):
        total1 += copy_arr1[i] * (3 ** (len(arr) - i - 1))
        total2 += copy_arr2[i] * (3 ** (len(arr) - i - 1))
    
    # 만약 가능한 케이스에 있으면 결과값 입력
    for num in case:
        if num == total1 or num == total2:
            result = num


# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # cost_2 : 2진수, cost_3 : 3진수
    cost_2 = list(map(int,list(input())))
    cost_3 = list(map(int,list(input())))

    # case : 가능한 송금액
    case = []
    result = 0
    
    # 2진수를 바꾸어 가능한 송금액 모두 구하기
    for i in range(len(cost_2)):
        bin_cost(cost_2, i)

    # 3진수를 바꾸어 가능한 송금액이 이미 앞에서 구한 case 에 있다면
    # 결과값으로 입력
    for j in range(len(cost_3)):
        ter_cost(cost_3, j)
        if result:
            break
    
    # 출력
    print('#{} {}'.format(test_case, result))