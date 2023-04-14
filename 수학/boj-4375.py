while True:
    try:
        N = int(input())
    except EOFError:
        break
    cur_number = 0
    cnt = 1
    while True: 
        cur_number = cur_number * 10 + 1
        cur_number %= N
        if cur_number == 0:
            print(cnt)
            break
        cnt+=1