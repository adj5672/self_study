data = input()
data = data.split('-')
for i in range(len(data)):
    data[i] = data[i].split('+')
    data[i] = sum(list(map(int, data[i])))
if len(data) == 1:
    print(data[0])
else:
    total = data[0]
    for i in range(1, len(data)):
        total -= data[i]
    print(total)
