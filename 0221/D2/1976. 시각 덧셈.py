T = int(input())

for tc in range(1, T+1):

    aa = list(map(int, input().split()))

    a = [aa[0], aa[1]]
    b = [aa[2], aa[3]]

    am = a[0] * 60 + a[1]
    bm = b[0] * 60 + b[1]

    c = am + bm
    h = c // 60
    if h > 12:
        h -= 12
    m = c % 60
    print('#{} '.format(tc), end='')
    print(h, m)