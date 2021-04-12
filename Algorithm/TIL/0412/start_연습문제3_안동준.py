# 입력 데이터
input_text = '0269FAC9A0'

h = '0123456789ABCDEF'

# 암호비트패턴
code = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

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

# 뒤에서부터 처음 1이 나오는 index 찾기
for idx in range(-1,-len(arr)-1, -1):
    if arr[idx] == 1:
        s_idx = idx
        break

# 뒤에서 부터 6개씩 slicing 해서 복호화
for idx in range(s_idx, -len(arr)-1, -6):
    data = ''.join(list(map(str,arr[idx-5:idx+1])))
    if len(data) == 6:
        for i, c in enumerate(code):
            if data == c:
                result.append(i)

# 출력
print(', '.join(list(map(str,list(reversed(result))))))
