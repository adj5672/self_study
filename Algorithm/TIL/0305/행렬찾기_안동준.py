# 화학 용기를 찾아 행과 열을 반환하는 함수
def s_mat(i,j):
    size = [0, 0]
    # 화학 용기의 열 길이
    for y in range(n):
        if j + y + 1 >= n or container[i][j+y+1] == 0:
            size[1] = y + 1
            break
    # 화학 용기의 행 길이
    for x in range(n):
        if i + x + 1 >= n or container[i+x+1][j] == 0:
            size[0] = x + 1
            break
    # 화학 용기의 행과 열 반환
    return size

# 화학 용기를 지우는 함수
def del_mat(i,j,x,y):

    for a in range(x):
        for b in range(y):
            container[i+a][j+b] = 0

# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # n : 화학 물질 용기 크기 (n * n)
    n = int(input())
    
    # 화학용기 만들기
    container = [list(map(int,input().split())) for _ in range(n)]
    
    # count : 화학 용기의 갯수, result : 화학 용기의 행과 열
    count = 0
    sub_result = []
    
    # 화학용기 찾기
    for x in range(n):
        for y in range(n):
            # 만약 화학용기의 좌측 상단좌표를 발견하면
            if container[x][y]:
                # 화학 용기의 행 열 크기를 받아
                size = s_mat(x,y)
                # 결과값에 append 하고
                sub_result.append(size)
                # 화학 용기의 갯수 + 1
                count += 1
                # 확인한 화학 용기는 지운다.
                del_mat(x,y,size[0],size[1])

    # 화학 용기 크기에 따라 정렬하기 (버블 정렬)
    for i in range(len(sub_result) - 1):
        for j in range(len(sub_result) - 1):
            # 크기 순서가 바뀐 경우
            if sub_result[j][0] * sub_result[j][1] > sub_result[j+1][0] * sub_result[j+1][1]:
                sub_result[j], sub_result[j+1] = sub_result[j+1], sub_result[j]
            # 크기가 같은 경우
            elif sub_result[j][0] * sub_result[j][1] == sub_result[j+1][0] * sub_result[j+1][1]:
                if sub_result[j][0] > sub_result[j+1][0]:
                    sub_result[j], sub_result[j + 1] = sub_result[j + 1], sub_result[j]

    # 출력할 형식에 맞게 배열 정리
    result = [count]
    for i in range(len(sub_result)):
        result.append(sub_result[i][0])
        result.append(sub_result[i][1])

    # 출력
    print('#{} {}'.format(test_case, ' '.join(map(str,result))))
