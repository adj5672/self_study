num = 456789
c = [0] * 12

for i in str(num):
    c[int(i)] += 1

run, triplet = 0, 0

for idx in range(10):
    for _ in range(2):
        if c[idx] >= 1 and c[idx+1] >= 1 and c[idx+2] >= 1:
            run += 1
            c[idx], c[idx+1], c[idx+2] = c[idx]-1, c[idx+1]-1, c[idx+2]-1
        elif c[idx] >= 3:
            triplet += 1
            c[idx] -= 3

if run + triplet == 2:
    print('bcby_gin')