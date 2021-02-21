T = int(input())

for tc in range(1, T + 1):

    NS = list(map(int, input().split()))

    for N in NS:

        arr = [[0 for col in range(N)] for row in range(N)]

        direction = 1
        num = 0
        north, east, south, west = 0, 0, 0, 0
        last_x = 0
        last_y = 0

        a = 0

        for i in range(N):
            num += 1
            arr[0][i] = num
            direction += 1
            last_x = i

        north += 1

        while num < N ** 2 + 1:

            for i in range(1, N - east * 2):
                num += 1
                arr[i + last_y][last_x] = num
                a = i + last_y
            last_y = a
            east += 1
            if num == N ** 2:
                break
            for i in range(1, N - south * 2):
                num += 1
                arr[last_y][last_x - i] = num
                a = last_x - i
            last_x = a
            south += 1
            if num == N ** 2:
                break
            for i in range(1, N - west * 2 - 1):
                num += 1
                arr[last_y - i][last_x] = num
                a = last_y - i
            last_y = a
            west += 1
            if num == N ** 2:
                break
            for i in range(1, N - north * 2 + 1):
                num += 1
                arr[last_y][last_x + i] = num
                a = last_x + i
            last_x = a
            north += 1
            if num == N ** 2:
                break

        print('#{}'.format(tc))
        for i in range(N):
            for j in range(N):
                print('{}'.format(arr[i][j]), end=' ')
            print()