def check_how_many_one(num):
    cnt = 0
    while num !=0:
        num, mod = divmod(num,2)
        if mod == 1:
            cnt+=1
    return cnt
def solution(n):
    one_cnt_now = check_how_many_one(n)
    n+=1
    while True:
        one_cnt_next = check_how_many_one(n)
        if one_cnt_next == one_cnt_now:
            return n
        n+=1
    
print(solution(78))