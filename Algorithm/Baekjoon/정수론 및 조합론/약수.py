N = int(input())
div = list(map(int,input().split()))
M = max(div) + 1

while True:
    for n in div:
        if M % n != 0:
            M += 1
            break
    else:
        print(M)
        break