# 같은 숫자는 시러요


def solution(arr):
    answer = []
    a = 10
    for i in arr:
        if i != a:
            answer.append(i)
            a = i
    return answer