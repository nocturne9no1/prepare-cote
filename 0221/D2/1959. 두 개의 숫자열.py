T = int(input())
# T = 1
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    if len(list_a) < len(list_b):

        # list a 에 0 추가하기 전에 미리 곱셈을 위한 수 알아두자
        com = len(list_a)
        # 최대인지?
        max_comsum = 0
        # list a 가 더 짧으니 일단 뒤에 0을 채워넣어 list b 와 길이를 맞춘다
        for zero_insert in range(len(list_b) - len(list_a)):
            list_a.append(0)

        # 곱 덧셈은 M-N 이면 된다.
        for i in range(len(list_b) - com + 1):
            # print(list_a, list_b)
            # 곱해서 더한 값 저장할 변수
            comsum = 0
            for j in range(com):
                # print(list_a[i + j], list_b[i + j])
                comsum += list_a[i + j] * list_b[i + j]
            if max_comsum < comsum:
                max_comsum = comsum
            # 한 턴 끝나면 작은 리스트 (현재는 a) 를 한칸씩 밀어주자 / a 가 더 길어져도 상관없으니 굳이 pop은 안해도 될지도
            list_a.insert(0, 0)

    elif len(list_a) > len(list_b):

        # list b 에 0 추가하기 전에 미리 곱셈을 위한 수 알아두자
        com = len(list_b)
        # 최대인지?
        max_comsum = 0
        # list b 가 더 짧으니 일단 뒤에 0을 채워넣어 list a와 길이를 맞춘다
        for zero_insert in range(len(list_a) - len(list_b)):
            list_b.append(0)

        # 곱 덧셈은 N-M 이면 된다.
        for i in range(len(list_a) - com + 1):
            # 곱해서 더한 값 저장할 변수
            comsum = 0
            for j in range(com):
                comsum += list_b[i + j] * list_a[i + j]
            if max_comsum < comsum:
                max_comsum = comsum
            # 한 턴 끝나면 작은 리스트 (현재는 b) 를 한칸씩 밀어주자 / b 가 더 길어져도 상관없으니 굳이 pop은 안해도 될지도
            list_b.insert(0, 0)

    answer = '#{} {}'.format(tc, max_comsum)
    print(answer)