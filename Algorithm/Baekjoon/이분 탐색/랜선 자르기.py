K, N = map(int, input().split())
data = []
for _ in range(K):
    data.append(int(input()))
data.sort()

maxValue, minValue = data[-1], 1

while minValue <= maxValue:

    middleValue = (minValue + maxValue) // 2

    total = 0
    for num in data:
        total += num // middleValue

    if total < N:
        maxValue = middleValue - 1
    elif total >= N:
        minValue = middleValue + 1

for num in data:
    N -= num // minValue

if N:
    print(maxValue)
else:
    print(minValue)
