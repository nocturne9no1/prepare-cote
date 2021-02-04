def solution(answers):
    answer = []
    soopo_a = [1, 2, 3, 4, 5]  # 5
    count_a = 0
    soopo_b = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    count_b = 0
    soopo_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    count_c = 0
    for idx, dab in enumerate(answers):
        if dab == soopo_a[idx % 5]:
            count_a += 1
        if dab == soopo_b[idx % 8]:
            count_b += 1
        if dab == soopo_c[idx % 10]:
            count_c += 1
    
    count_list = [count_a, count_b, count_c]
    max_count = 0
    max_count = max(count_list)
    if count_a == max_count:
        answer.append(1)
    if count_b == max_count:
        answer.append(2)
    if count_c == max_count:
        answer.append(3)
    return answer