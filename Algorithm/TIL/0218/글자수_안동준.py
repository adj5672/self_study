# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    str1 = input()
    str2 = input()

    # str1에 포함되어 있는 글자 list 생성
    words = []
    for i in range(len(str1)):
        for j in range(len(str1)-i):
            words.append(str1[j:j+i+1])

    # 각 글자마다 str2에 몇 개씩 들어있는지 count 하기
    count = [0 for _ in range(len(words))]
    for idx, word in enumerate(words):
        n = len(word)
        for i in range(len(str2)-n+1):
            if word == str2[i:i+n]:
                count[idx] += 1

    # 최댓값 확인하기
    max_count = 0
    for num in count:
        if num > max_count:
            max_count = num

    # 출력
    print('#{} {}'.format(test_case,max_count))