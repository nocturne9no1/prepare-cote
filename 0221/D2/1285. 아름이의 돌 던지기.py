# 다 풀었더니 파이썬 지원 안함 ㅋㅋㅋㅋ

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    throw = list(map(int, input().split()))
    distances = []
    closest = 999999999


    for i in range(N):
        if throw[i] >= 0:
            distances.append(throw[i])
        else:
            distances.append(throw[i] * -1)

        if closest > distances[i]:
            closest = distances[i]
    count = 0
    for i in range(N):
        if closest == distances[i]:
            count += 1

    print('#{} {} {}'.format(tc, closest, count))
