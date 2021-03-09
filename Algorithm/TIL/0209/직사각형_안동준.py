for test_case in range(4):
    rectangles = list(map(int,input().split()))
    rec1, rec2 = rectangles[:4], rectangles[4:]
    if rec1[2] < rec2[0] or rec2[2] < rec1[0] or rec1[3] < rec2[1] or rec2[3] < rec1[1]:
        print('d')
    elif rec1[2:] == rec2[:2] or rec2[2:] == rec1[:2] or (rec1[1] == rec2[3] and rec1[2] == rec2[0]) or (rec2[1] == rec1[3] and rec2[2] == rec1[0]):
        print('c')
    elif rec1[0] == rec2[2] or rec2[0] == rec1[2] or rec1[1] == rec2[3] or rec2[1] == rec1[3]:
        print('b')
    else:
        print('a')