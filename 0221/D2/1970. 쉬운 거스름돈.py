T = int(input())

for tc in range(1, T+1):
    m = int(input())

    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):
        cnt[i] = m // coin[i]
        m %= coin[i]
    print('#{}'.format(tc))
    print(' '.join(map(str, cnt)))