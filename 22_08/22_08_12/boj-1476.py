limit_e = 15
limit_s = 28
limit_m = 19

E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
cnt = 1
while e != E or s != S or m != M:
    if e == limit_e:
        e = 0
    if s == limit_s:
        s = 0
    if m == limit_m:
        m = 0
    e+=1
    s+=1
    m+=1
    cnt+=1
print(cnt)