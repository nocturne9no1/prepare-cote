T = int(input())

for tc in range(1, T+1):

    b = input().split()
    b[9] = b[9].replace(" ", "")
    arr = list(map(int, b))

    max_num = 0
    min_num = 100001

    for i in arr:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    # print(max_num)
    # print(min_num)
    total = 0
    for i in arr:
        total += i

    total -= max_num + min_num
    print('#{} '.format(tc), end='')
    print(round(total / 8))