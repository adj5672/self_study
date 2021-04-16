# test_case 갯수
T = int(input())

# 지불 가능 지폐
bill = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
n = len(bill)

for test_case in range(1,T+1):
    # money : 지불해야 하는 금액
    money = int(input())

    # pay : 지불할 지폐 갯수
    pay = [''] * n

    for i in range(n):
        pay[i] = str(money // bill[i])
        money = money % bill[i]

    # 출력
    print('#{}'.format(test_case))
    print(' '.join(pay))