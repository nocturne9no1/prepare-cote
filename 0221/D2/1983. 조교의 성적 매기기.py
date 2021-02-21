def score(a):
    return 35 * a[0] + 45 * a[1] + 20 * a[2]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [[] for _ in range(N)]
    score_list = []
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        score_list.append(score(arr[i]))


    # 순위 매기기
    # 이게 순위 매기는 좋은 방법일 것인가? 이중 포문이라 효율적이지는 않은 것 같다
    rank = [0] * N
    for i in range(N):
        temp = 0
        for j in range(N):
            if i != j:
                if score_list[i] > score_list[j]:
                    temp += 1
        rank[i] = N - temp

    a_score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']

    # K 번째 학생의 랭크 = rank(K-1)

    print('#{} '.format(tc), end='')
    if rank[K-1] < N * 0.1:
        print('A+')
    elif rank[K-1] <= N * 0.2:
        print('A0')
    elif rank[K-1] <= N * 0.3:
        print('A-')
    elif rank[K-1] <= N * 0.4:
        print('B+')
    elif rank[K-1] <= N * 0.5:
        print('B0')
    elif rank[K-1] <= N * 0.6:
        print('B-')
    elif rank[K-1] <= N * 0.7:
        print('C+')
    elif rank[K-1] <= N * 0.8:
        print('C0')
    elif rank[K-1] <= N * 0.9:
        print('C-')
    else:
        print('D')

# print(arr)
# print(score_list)
# print(rank)
# print(rank[K-1])