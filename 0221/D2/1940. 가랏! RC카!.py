T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [[0] for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    speed = 0
    move = 0

    for i in range(N):
        #가속
        if arr[i][0] == 1:
            speed += arr[i][1]
            move += speed

        # 감속
        elif arr[i][0] == 2:
            speed -= arr[i][1]
            if speed < 0:
                speed = 0
            move += speed

        # 현 속도 유지
        elif arr[i][0] == 0:
            move += speed

    print('#{} {}'.format(tc, move))