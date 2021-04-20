data = input()
map_data = []
operator = ['+', '-']

i = 0
while i < len(data):
    if data[i] not in operator:
        num = ''
        while data[i] not in operator:
            num += data[i]
            i += 1
            if i == len(data):
                break
        map_data.append(int(num))
    else:
        map_data.append(data[i])
        i += 1

plus_result = []

j = 0
while j < len(map_data) - 2:
    if map_data[j+1] != '+':
        plus_result.append(map_data[j])
        j += 1
    else:
        num = map_data[j] + map_data[j+2]
        plus_result.append(num)
        j += 3

print(eval(''.join(list(map(str,plus_result)))))