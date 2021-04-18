import sys

# 회의 갯수
N = int(input())

# 회의 정보
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 배정할 회의
result = []
end_time = 0

# 종료시간 기준 정렬 (오름차순)
data.sort(key=lambda x: (x[1], x[0]))

while data:
    meeting = data.pop(0)
    if meeting[0] >= end_time:
        result.append(meeting)
        end_time = meeting[1]

print(len(result))