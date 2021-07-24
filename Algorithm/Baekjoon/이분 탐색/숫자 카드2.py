from collections import Counter

N = int(input())
myCards = input().split()
M = int(input())
data = input().split()

dictData = Counter(myCards)
data = list(map(lambda x: str(dictData[x]), data))
print(' '.join(data))
