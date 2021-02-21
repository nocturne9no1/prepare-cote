# txt 오픈 세팅으로 넣어보자
# 앞에서 부터 가면 시관 초과 뜰 수 밖에
# D2 에서 가장 난이도 있다.
# 뒤에서부터 라는 생각을 하기 까지가 쉽지 않을 것
# 규칙을 찾아보자

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    sise = list(map(int, input().split()))
    max_price = sise[N-1]
    max_idx = 0
    ideuk = 0

    for i in range(N-1,-1,-1):
        if max_price - sise[i] > 0:
            ideuk += max_price - sise[i]
        if max_price < sise[i]:
            max_price = sise[i]
        #
        #
        #
        # for idx, price in enumerate(sise):
        #     if max_price < price:
        #         max_price = price
        #         max_idx = idx
        #
        # for i in range(max_idx):
        #     ideuk += max_price - sise[i]
        #
        # for i in range(max_idx+1):
        #     sise.pop(0)
        #
        # max_price = 0
        # max_idx = 0

    print('#{} {}'.format(tc, ideuk))


    # ValueError: invalid literal for int() with base 10:
    # 인풋으로 하나만 넣을거야 했는데
    # 너무 많은 걸 넣을려고 하고 있어
    # 정석적으로 따지면 (tc->)1, 원소의 개수, 리스트가 들어오는 것임