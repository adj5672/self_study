# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N, L = map(int,input().split())
    # 햄버거 재료들 list 정리
    ingredients = []
    for _ in range(N):
        ingredients.append(list(map(int,input().split())))

    # 최고의 맛 점수
    max_taste = 0

    # 재료들로 만들수 있는 조합(부분집합) 생성
    for i in range(1 << N):
        burger, taste, cal = [], 0, 0
        for j in range(N):
            if i & (1 << j):
                burger.append(ingredients[j])
        # 각 burger로 부터 맛 점수와 칼로리 계산
        for ingredient in burger:
            taste += ingredient[0]
            cal += ingredient[1]
        # 칼로리 상한선을 넘지 않는 burger에 대해 맛 점수비교
        if cal <= L and taste >= max_taste:
            max_taste = taste

    # 출력
    print('#{} {}'.format(test_case,max_taste))
