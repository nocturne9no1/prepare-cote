T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    charge_a = 0
    charge_b = 0

    # A 요금 구해보자
    charge_a = W * P

    # B 요금을 구해보자
    if W <= R:
        charge_b = Q
    else:
        charge_b = Q + (W - R) * S
    print('#{} '.format(tc), end='')
    # A B 요금 비교
    if charge_a < charge_b:
        print(charge_a)
    else:
        print(charge_b)