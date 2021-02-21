# 회문이면 1, 아니면 0

T = int(input())

for tc in range(1, T+1):

    string = list(input())

    answer = 1

    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            answer = 0
            break

    print('#{} {}'.format(tc, answer))