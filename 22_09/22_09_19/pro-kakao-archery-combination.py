from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1
    # 중복 조합을 통해 화살을 다섯번 쏘는 모든 상황을 구한다.
    for combi in combinations_with_replacement(range(11), n):
        ryan_info = [0]*11
        # 쏜 화살을 반영시킨 후
        for i in combi:
            ryan_info[10-i] += 1
        
        apeach, ryan = 0, 0
        for idx in range(11):
            # 둘 다  0이면 넘어가고
            if info[idx] == ryan_info[idx] == 0:
                continue
            # 어피치가 크면 어피치의 점수를 높여주고
            elif info[idx] >= ryan_info[idx]:
                apeach += 10 - idx
            # 아니라면 라이언의 점수를 높인다.
            else: ryan += 10 - idx
        
        # 점수를 확인하고 라이언이 더 크면
        # max_gap을 변경해주고 anwer에 지금 값을 할당
        if ryan > apeach:
            gap = ryan - apeach
            if gap > max_gap:
                max_gap = gap
                answer = ryan_info
    return answer