def solution(S,P,Q):
    factor_map = {
        "A" : 1,
        "C" : 2,
        "G" : 3,
        "T" : 4
    }
    answer = []
    for p, q in zip(P, Q):
        min_num = 5
        for key in factor_map.keys():
            if key in S[p:q+1]:
                min_num = min(min_num, factor_map[key])
        answer.append(min_num)      
    return answer