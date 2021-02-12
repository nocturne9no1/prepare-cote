
# 삼각 달팽이

def solution(n):
    answer = []
    tower = [0] * n
    for i in range(n):
        tower[i] = [0] * n
    num = 0
    forbreak = 0
    tx = 0
    ty = 0
    # 숫자의 끝은 n+(n-1)+(n-2)+....+2+1 이다
    for i in range(1, n + 1):
        forbreak += i
    # 한바퀴 돌면 세로축 하나가 밀림
    x = 0
    # 한바퀴 돌면 가로축 하나 위로 올라옴
    y = 0
    while num < forbreak+1:
        # 내려가는 달팽이
        for i in range(n-y*2-x):
            num += 1
            tower[i+y*2][x] = num
            if num == forbreak:
                break
        if num == forbreak:
            break
        # 우향하는 달팽이
        for i in range(n-x*2-y-1):
            num += 1
            tower[n - 1 - y][i+1+x] = num
            tx = n-1-y
            ty = i+1+x
            if num == forbreak:
                break
        if num == forbreak:
            break
        i = 0
        # 올라가는 달팽이
        while tower[tx-i-1][ty-i-1] == 0:
            num += 1
            tower[tx-i-1][ty-i-1] = num
            i += 1
            if num == forbreak:
                break
        if num == forbreak:
            break
        x += 1
        y += 1

    # answer 에 옮겨담자
    for i in range(n):
        for j in range(i + 1):
            answer.append(tower[i][j])

    return answer