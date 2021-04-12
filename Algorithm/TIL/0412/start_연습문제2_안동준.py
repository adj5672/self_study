# 입력 데이터
input_text = '0F97A3'

h = '0123456789ABCDEF'

arr = []
result = []

# 16진수를 2진수로 변환
for word in input_text:
    num = h.find(word)
    for i in range(3, -1, -1):
        if num & (1 << i):
            arr.append(1)
        else:
            arr.append(0)

# 7개씩 slicing
for idx in range(0, len(arr), 7):
    data = arr[idx:idx+7]
    num = 0
    # 10진수로 변환
    for i in range(0, len(data)):
        if data[-i-1]:
            num += (1 << i)
    result.append(num)

# 출력
print(', '.join(list(map(str,result))))