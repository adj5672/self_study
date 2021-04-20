N = int(input())

people = list(map(int,input().split()))
people.sort()

total = 0

for i in range(N):
    total += sum(people[:i+1])

print(total)