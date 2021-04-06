# test_case 갯수
T = int(input())

# 각 월별 날 수
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1,T+1):
    days = list(map(int,input().split()))
    day1 = sum(month[:days[0]-1]) + days[1]
    day2 = sum(month[:days[2]-1]) + days[3]
    print('#{} {}'.format(test_case,day2-day1+1))