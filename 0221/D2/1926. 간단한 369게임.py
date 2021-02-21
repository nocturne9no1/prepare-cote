N = int(input())

arr = [i for i in range(1, N+1)]
sam = [3, 6, 9]

for i in range(N):

    temp = arr[i]
    temp_arr = []

    while temp > 0:
        temp_arr.append(temp % 10)
        temp //= 10

    three_cnt = 0
    for j in range(len(temp_arr)):
        if temp_arr[j] in sam:
            three_cnt += 1

    if three_cnt == 0:
        print(arr[i], end=' ')
    else:
        print('-'*three_cnt, end=' ')