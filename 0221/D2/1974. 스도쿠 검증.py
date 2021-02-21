# 세 가지 검증
# 1. 가로 한줄씩    2. 세로 한줄씩    3. 3X3 네모칸 9개 검증

T = int(input())

for tc in range(1, T+1):

    arr = [[] for _ in range(9)]

    for i in range(9):
        arr[i] = list(map(int, input().split()))

    # print(arr)

    answer = 1

    # 가로 검증
    for i in range(9):
        check = [0] * 9
        for j in range(9):
            check[arr[i][j]-1] += 1

        for j in range(9):
            if check[j] != 1:
                answer = 0

    # 세로 검증
    for i in range(9):
        check = [0] * 9
        for j in range(9):
            check[arr[j][i] - 1] += 1

        for j in range(9):
            if check[j] != 1:
                answer = 0

    # 3 X 3 검증
    aa = [0, 3, 6]
    for i in aa:
        check = [0] * 9
        for x in range(3):
            for y in range(3):
                check[arr[i+x][i+y]-1] += 1

        for x in range(9):
            if check[j] != 1:
                answer = 0

    print('#{} {}'.format(tc, answer))
