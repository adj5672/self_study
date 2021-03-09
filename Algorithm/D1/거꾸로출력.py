N = int(input())
result = []
for i in range(N,-1,-1):
    result.append(i)
print(' '.join(map(str,result)))