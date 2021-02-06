# 문자열 다루기 기본

def solution(s):
    answer = True
    int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if (len(s) == 4 or len(s) == 6):
        for chr in s:
            if chr not in int_list:
                answer = False
                break
    else:
        answer = False
    return answer