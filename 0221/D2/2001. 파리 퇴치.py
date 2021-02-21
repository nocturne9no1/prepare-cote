T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    dfs = [0 for i in range(N)]


    for i in range(N):
        dfs[i] = list(map(int, input().split()))

    best_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            df_kill = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    df_kill += dfs[x][y]

            if best_kill < df_kill:
                best_kill = df_kill

    print('#{} {}'.format(tc, best_kill))