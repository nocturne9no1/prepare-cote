# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
#
T = int(input())

for tc in range(1, T+1):

    monthly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    a = list(map(int, input().split()))

    before = [a[0], a[1]]
    after = [a[2], a[3]]

    before_m_day = 0
    after_m_day = 0

    for i in range(before[0]-1):
        before_m_day += monthly[i]
    before_m_day += before[1]

    for i in range(after[0]-1):
        after_m_day += monthly[i]
    after_m_day += after[1]

    answer = after_m_day - before_m_day + 1
    print('#{} {}'.format(tc, answer))