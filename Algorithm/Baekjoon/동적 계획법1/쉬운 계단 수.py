N = int(input())
i = 1
count = [0 for _ in range(10)]
for j in range(1,10):
    count[j] = 1

while i < N:
    new_count = [0 for _ in range(10)]
    new_count[0] = count[1]
    new_count[9] = count[8]
    for k in range(1,9):
        new_count[k] = count[k-1] + count[k+1]
    count = [x for x in new_count]
    i += 1

print(sum(count) % (10 ** 9))
