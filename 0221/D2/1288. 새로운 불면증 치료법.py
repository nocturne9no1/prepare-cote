T = int(input())

for tc in range(1, T+1):
    N = int(input())

    zero_to_nine = []
    count = 1

    while True:
        temp = N * count
        one_by_one = []
        while temp > 0:
            one_by_one.append(temp % 10)
            temp //= 10
        for i in range(len(one_by_one)):
            if one_by_one[i] not in zero_to_nine:
                zero_to_nine.append(one_by_one[i])
        if len(zero_to_nine) == 10:
            break
        count += 1

    print('#{} {}'.format(tc, count * N))