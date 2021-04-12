# 1차 배열에서 7 byte를 묶어 10진수로 출력

# 입력 데이터
arr = [
    0,0,0,0,0,0,0,1,1,1,
    1,0,0,0,0,0,0,1,1,0,
    0,0,0,0,0,1,1,1,1,0,
    0,1,1,0,0,0,0,1,1,0,
    0,0,0,1,1,1,1,0,0,1,
    1,1,1,0,0,1,1,1,1,1,
    1,0,0,1,1,0,0,1,1,1
]

result = []

for idx in range(0,len(arr),7):
    # 7개씩 slicing
    data = arr[idx:idx+7]
    num = 0
    for i in range(7):
        if data[6-i]:
            num += 2 ** i
    result.append(num)

# 출력
print(', '.join(list(map(str,result))))
