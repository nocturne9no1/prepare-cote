T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    counting = [0 for i in range(101)]
    max_num = 0
    max_i = 0
    for i in students:
        counting[i] += 1

    for idx, i in enumerate(counting):
        if max_i <= i:
            max_num = idx
            max_i = i

    print('#{} {}'.format(tc, max_num))