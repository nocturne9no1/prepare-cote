# 홀수는 다 더하고 짝수는 다 빼고

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    sum  = 0

    for i in range(1, N+1):
        if i % 2 == 1:
            sum += i
        else:
            sum -= i

    print('#{} {}'.format(tc, sum))
