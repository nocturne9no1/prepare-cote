T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] for _ in range(N)]

    total_cnt = 0

    for i in range(N):
        arr[i] = list(input().split())
        total_cnt += int(arr[i][1])

    ten = [[] for _ in range(total_cnt//10 + 1)]
    string = []


    for i in range(N):
        for j in range(int(arr[i][1])):
            string.append(arr[i][0])

    idx = 0
    row = 0
    full = 0
    while full < total_cnt:
        ten[row].append(string[full])
        idx += 1
        full += 1
        if idx == 10:
            idx = 0
            row += 1

    print('#{}'.format(tc))
    for i in range(len(ten)):
        print(''.join(ten[i]))

