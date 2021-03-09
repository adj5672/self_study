T = int(input())

for test_case in range(T):
    max = 0
    N = int(input())
    Arr = list(map(int,input().split()))
    for idx, num in enumerate(Arr):
        count = 0
        for i in Arr[idx+1:]:
            if num > i:
                count += 1
        if count > max:
            max = count
    print(max)