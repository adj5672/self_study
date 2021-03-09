for test_case in range(1,11):
    count = 0
    N = int(input())
    apt = list(map(int,input().split()))
    for i in range(2,N-2):
        view = apt[i]
        if apt[i-2] < apt[i] and apt[i-1] < apt[i] and apt[i+1] < apt[i] and apt[i+2] < apt[i]:
            for j in range(i-2,i+3):
                if j != i and apt[i] - apt[j] < view:
                    view = apt[i] - apt[j]
        else:
            view = 0
        count += view
    print('#{} {}'.format(test_case,count))