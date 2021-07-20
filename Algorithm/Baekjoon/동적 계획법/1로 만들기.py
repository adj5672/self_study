N = int(input())
i = 0
cal = [N]

while 1 not in cal:
    new_cal = []
    for num in cal:
        if num % 3 == 0:
            new_cal.append(num // 3)
        if num % 2 == 0:
            new_cal.append(num // 2)
        new_cal.append(num-1)
    cal = [x for x in new_cal]
    i += 1

print(i)

