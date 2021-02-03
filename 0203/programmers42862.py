# 내 코드
def solution(n, lost, reserve):
    answer = 0
    # 일단 잃어버린 사람은 못빌려줘용
    real_reserve = list(set(reserve) - set(lost))
    real_lost = list(set(lost) - set(reserve))
    # 일어버린 사람 손
    for i in real_lost:
        # 빌려줄 사람 손
        for j in real_reserve:
            
            # 빌려줄 사람아 잃어버린 사람 사이즈 ㄱㄴ?
            # 일단 왼쪽 사람한테 물어봐바
            if i - 1 == j:
                # ㄱㄴ!
                answer += 1
                # 빌려줬으면 나가!
                real_reserve.remove(j)
                
            # 왼쪽 사람 없대? 그럼 오른쪽 사람?
            elif i + 1 == j:
                # ㄱㄴ!
                answer += 1
                # 빌려줬으면 나가!
                real_reserve.remove(j)
    
    return n - len(real_lost) + answer


# 예지님 코드를 응용하여 작성한 코드 (enumerate 응용)
def solution(n, lost, reserve):
    # 진짜 잃어버린 사람을 찾아서 n에서 빼자
    real_lost = 0 
    
    for i, lost_student in enumerate(lost):
        for j, reserve_student in enumerate(reserve):
            if reserve_student == lost_student:
                reserve[j] = -1
                lost[i] = -1
                break
    
    for i, lost_student in enumerate(lost):
        for j, reserve_student in enumerate(reserve):
            if (reserve_student==lost_student+1 or reserve_student==lost_student-1):
                reserve[j] = -1
                lost[i] = -1
                break
        if lost[i] != -1:
            real_lost += 1
            
    answer = n - real_lost
    return answer