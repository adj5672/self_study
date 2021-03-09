# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    time = 0

    # 돌아가야 할 방 번호
    students = []
    for _ in range(N):
        students.append(list(map(int,input().split())))

    # 학생들이 지나가는 복도를 나타낸 배열
    # hall의 i번째 index는 room(2*i+1)과 room(2*i+2) 앞 복도이다.
    hall = [0 for _ in range(200)]

    # 각 방 앞 복도마다 지나가는 학생수를 count
    for student in students:

        # start : 현재 방 앞의 복도 index
        if student[0] % 2:
            start = student[0] // 2
        else:
            start = student[0] // 2 - 1

        # end : 돌아갈 방의 복도 index
        if student[1] % 2:
            end = student[1] // 2
        else:
            end = student[1] // 2 - 1

        # 각 학생마다 복도를 지나 이동한다.
        if end >= start:
            for move in range(start, end+1):
                hall[move] += 1
        else:
            for move in range(end, start+1):
                hall[move] += 1

    # 각 단위시간 마다 학생들이 겹치지 않게 이동하므로
    # 복도에 지나가야할 학생이 없을 때 까지 단위시간 마다 복도를 지나간 학생수들을 모두 -1
    # 총 걸린 시간을 count
    # 결국 복도에 존재하는 최댓값과 같다.
    count = max(hall)

    # 출력
    print('#{} {}'.format(test_case, count))
