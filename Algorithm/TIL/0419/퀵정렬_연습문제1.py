'''
input_data
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0
'''

# Lomuto (arr : 배열, p : partition 시작 인덱스, r : 피봇 인덱스, partition 마지막 인덱스)
def Lomuto(arr, p, r):

    # partition 의 크기가 1 이하인 경우
    if p >= r:
        return

    # x : 피봇
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    
    # 피봇의 좌측 partition 정렬
    Lomuto(arr, p, i)
    # 피봇의 우측 partition 정렬
    Lomuto(arr, i+1, r)

arr = list(map(int,'11 45 23 81 28 34'.split()))
Lomuto(arr, 0, len(arr)-1)
print(arr)

arr = list(map(int,'11 45 22 81 23 34 99 22 17 8'.split()))
Lomuto(arr, 0, len(arr)-1)
print(arr)

arr = list(map(int,'1 1 1 1 1 0 0 0 0 0'.split()))
Lomuto(arr, 0, len(arr)-1)
print(arr)