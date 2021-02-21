# 파스칼 삼각형 만들기
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[] for _ in range(N)]

    for i in range(N):
        pascal[i] = [0] * N

    pascal[0][0] = 1

    for i in range(1, N):
        for j in range(N):
            if j == 0 or j == N-1:
                pascal[i][j] = 1
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        print()

