# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    count = 0
    
    # 색칠할 사각형들 모으기
    squares = []
    for _ in range(N):
        squares.append(list(map(int,input().split())))

    # 평면 만들기
    plane = [['' for _ in range(10)] for _ in range(10)]

    # 평면에 색칠하기
    for square in squares:
        for r in range(square[0], square[2]+1):
            for c in range(square[1], square[3]+1):
                if square[4] == 1:
                    plane[r][c] += 'r'
                else:
                    plane[r][c] += 'b'
                    
    # plane 순회하며 색이 겹친부분 counting 하기
    for i in range(10):
        for j in range(10):
            if 'r' in plane[i][j] and 'b' in plane[i][j]:
                count += 1

    # 출력
    print('#{} {}'.format(test_case,count))