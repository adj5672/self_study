def maximum(lists):
    max = lists[0]
    for num in lists:
        if num > max:
            max = num
    return max

def minimum(lists):
    min = lists[0]
    for num in lists:
        if num < min:
            min = num
    return min

for test_case in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump):
        max_value, min_value = maximum(boxes), minimum(boxes)
        for idx, box in enumerate(boxes):
            if box == max_value:
                boxes[idx] -= 1
                break
        for idx, box in enumerate(boxes):
            if box == min_value:
                boxes[idx] += 1
                break
    print('#{} {}'.format(test_case,maximum(boxes)-minimum(boxes)))