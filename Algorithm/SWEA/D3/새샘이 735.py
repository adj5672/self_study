T = int(input())

for test_case in range(1,T+1):
    nums = list(map(int,input().split()))
    result = []
    # 세 정수의 합
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1,len(nums)):
                result.append(nums[i] + nums[j] + nums[k])
    # 중복 제거
    result = list(set(result))
    # 정렬
    result.sort()
    # 출력
    print('#{} {}'.format(test_case, result[-5]))