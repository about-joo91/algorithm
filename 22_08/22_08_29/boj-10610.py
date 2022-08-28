N = sorted(input(), reverse=True)
sum_of_num = 0
if '0' not in N:
    print(-1)
else:
    for num in N:
        sum_of_num += int(num)
    if sum_of_num % 3 ==0:
        print(''.join(N))
    else:
        print(-1)