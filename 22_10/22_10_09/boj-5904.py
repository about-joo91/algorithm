def get_alpha_of_moo(len_of_moo, cur_cnt, N):
    prev = (len_of_moo - (cur_cnt+3))//2
    if N <= prev: return get_alpha_of_moo(prev, cur_cnt-1, N)
    elif N > prev + (cur_cnt+3): return get_alpha_of_moo(prev, cur_cnt-1, N-prev-(cur_cnt+3))
    else: return "o" if N-prev-1 else "m"

N = int(input())
len_of_moo = 3
cnt = 0
while len_of_moo < N:
    cnt+=1
    len_of_moo = len_of_moo*2 + cnt+3
    
print(get_alpha_of_moo(len_of_moo, cnt, N))