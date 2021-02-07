# 신규 아이디 추천

def solution(new_id):
    answer = ''
    available_chrs = ['-', '_', '.']
    # 1단계 - 대문자 → 소문자
    a = list(new_id.lower())
    # 2단계 - 가능한 거 빼고 제거
    idx = 0
    while idx < len(a):
        if (a[idx].isalnum() == False and a[idx] not in available_chrs):
            a.pop(idx)
        else:
            idx += 1
    
    # 3단계 - . 2번 연속 하나로 치환
    idx = 0
    if len(a) > 2:
        while idx < len(a):
            if a[idx] == '.':
                if a[idx-1] == a[idx]:
                    a.pop(idx)
                else:
                    idx += 1
            else:
                idx += 1
    
    # 4단계 - . 이 처음이나 끝에 있다면 제거
    if len(a) > 0:
        if a[0] == '.':
            a.pop(0)
    if len(a) > 0:
        if a[len(a)-1] == '.':
            a.pop(len(a)-1)
    
    # 5단계 - 빈 문자열이면 a 대입
    if a == []:
        a = 'aaa'
    
    # 6단계 - 길이가 16 이상이면 앞에 15개만, 제거 후 앞뒤 . 제거
    if len(a) >= 16:
        a = a[0:15]
        if a[0] == '.':
            a.pop(0)
        if a[len(a)-1] == '.':
            a.pop(len(a)-1)
    
    # 7단계 - 길이 2 이하라면 마지막 문자 길이 3될 때 까지 반복
    if len(a) <= 2:
        while len(a) < 3:
            a.append(a[len(a)-1])
    
    answer = answer.join(a)
    return answer