num = list(map(int, list(input())))
cant30 = sum(num) % 3
if 0 not in num or cant30:
    print(-1)
else:
    num.sort(reverse=True)
    print(''.join(list(map(str, num))))
