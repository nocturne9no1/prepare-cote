# 문자열 길이 30
# 최대 길이 10

for tc in range(1, int(input())+1):

    arr = list(input())

    # print(arr)

    banbok_len = 1
    b = 1
    banbok = []
    stop = False

    while True:
        for i in range(b):
            banbok.append(arr[i])
        for i in range(b):
            if banbok[i] != arr[b+i]:
                break
        else:
            stop = True
        if stop == True:
            break
        else:
            b += 1
            banbok = []


    print('#{} {}'.format(tc, len(banbok)))

    # banbok_str = ''.join(banbok)
    #
    # print(banbok_str)
