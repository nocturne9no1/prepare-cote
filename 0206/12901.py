def solution(a, b):
    
    # 윤년 : 2월 29일 존재
    # 1:31 2:29 3:31 4:30 5:31 6:30
    # 7:31 8:31 9:30 10:31 11:30 12:31
    # 총 366일, 1주는 7일
    answer = ''
    days = 0
    # 요일 출력을 위한 요일 리스트 생성
    # 1월 1일이 금요일이기 때문에 1번 인덱스에 금요일 가도록 리스트 생성
    day_of_the_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    # 쌓아 올려 볼까
    if a == 1:
        answer = day_of_the_week[b % 7]
    else:
        days += 31
        if a == 2:
            answer = day_of_the_week[(days+b) % 7]
        else:
            days += 29
            if a == 3:
                answer = day_of_the_week[(days+b) % 7]
            else:
                days += 31
                if a == 4:
                    answer = day_of_the_week[(days+b) % 7]
                else:
                    days += 30
                    if a == 5:
                        answer = day_of_the_week[(days+b) % 7]
                    else:
                        days += 31
                        if a == 6:
                            answer = day_of_the_week[(days+b) % 7]
                        else:
                            days += 30
                            if a == 7:
                                answer = day_of_the_week[(days+b) % 7]
                            else:
                                days += 31
                                if a == 8:
                                    answer = day_of_the_week[(days+b) % 7]
                                else:
                                    days += 31
                                    if a == 9:
                                        answer = day_of_the_week[(days+b) % 7]
                                    else:
                                        days += 30
                                        if a == 10:
                                            answer = day_of_the_week[(days+b) % 7]
                                        else:
                                            days += 31
                                            if a == 11:
                                                answer = day_of_the_week[(days+b) % 7]
                                            else:
                                                days += 30
                                                if a == 12:
                                                    answer = day_of_the_week[(days+b) % 7]
                                                
    return answer