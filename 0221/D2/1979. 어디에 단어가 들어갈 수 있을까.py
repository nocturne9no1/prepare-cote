T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [0 for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    count = 0

    # 우선 행 단위로
    for i in range(N):
        space = 0
        for j in range(N):
            if arr[i][j] == 1:
                space += 1
            elif arr[i][j] == 0:
                if space == M:
                    count += 1
                space = 0
        else:
            if space == M:
                count += 1

    for j in range(N):
        space = 0
        for i in range(N):
            if arr[i][j] == 1:
                space += 1
            elif arr[i][j] == 0:
                if space == M:
                    count += 1
                space = 0
        else:
            if space == M:
                count += 1

    print('#{} {}'.format(tc, count))