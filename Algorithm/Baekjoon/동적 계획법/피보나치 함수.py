def fibo(n):

    if n == 0:
        return memo[0]

    elif n == 1:
        return memo[1]

    elif n >= len(memo):
        memo.append([fibo(n-1)[0] + fibo(n-2)[0], fibo(n-1)[1] + fibo(n-2)[1], fibo(n-1)[2] + fibo(n-2)[2] ])
    
    return memo[n]
    

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):

    n = int(input())

    memo = [[0, 1, 0], [1, 0, 1]]

    fibo(n)

    if n == 0:
        print(1,0)
    else:
        print(memo[-1][1], memo[-1][2])