T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[] for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # print(arr)
    turn_90 = [[] for _ in range(N)]
    turn_180 = [[] for _ in range(N)]
    turn_270 = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            turn_90[i].append(str(arr[N-j-1][i]))
            turn_180[i].append(str(arr[N-i-1][N-j-1]))
            turn_270[i].append(str(arr[j][N-i-1]))

    print('#{} '.format(tc))
    for i in range(N):
        print(''.join(turn_90[i]), ''.join(turn_180[i]), ''.join(turn_270[i]))
    # print(turn_90)
    # print(turn_180)
    # print(turn_270)