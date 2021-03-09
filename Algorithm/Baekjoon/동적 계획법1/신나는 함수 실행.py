def w(a, b, c):

    A, B, C = a + 50, b + 50, c + 50

    if memo[A][B][C] == False:

        if A > 70 or B > 70 or C > 70:
            memo[A][B][C] = w(19, 20, 20) + w(19, 19, 20) + w(19, 20, 19) - w(19, 19, 19)
            return memo[A][B][C]

        elif A < B and B < C:
            memo[A][B][C] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return memo[A][B][C]
        
        else:
            memo[A][B][C] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return memo[A][B][C]

    else:
        return memo[A][B][C]
            

memo = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]

for x in range(101):
    for y in range(101):
        for z in range(101):
            if type(memo[x][y][z]) == bool and  x < 51 or y < 51 or z < 51:
                memo[x][y][z] = 1 


while True:
    a, b, c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
