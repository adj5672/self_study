T = int(input())

for tc in range(1,T+1):
    N = input()
    if int(N[-1]) % 2 == 1:
        print('#{} Odd'.format(tc))
    else:
        print('#{} Even'.format(tc))