T = int(input())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1,T+1):
    date = input()
    m = int(date[4:6])
    d = int(date[6:])
    if m <= 0 or m >= 13 or d > month[m-1] or d <= 0:
        result = -1
    else:
        result = date[:4] + '/' + date[4:6] + '/' + date[6:]

    print('#{} {}'.format(test_case,result))