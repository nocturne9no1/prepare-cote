T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    for i in range(len(arr)-1):
        min_temp = i
        for j in range(i+1, len(arr)):
            if arr[min_temp] > arr[j]:
                min_temp = j
        arr[i], arr[min_temp] = arr[min_temp], arr[i]

    print('#{} '.format(tc), end='')
    for i in range(N):
        print(arr[i], end=' ')
    print()