BOY = 1
GIRL = 2

N = int(input())
switches = [0] + list(map(int, input().split()))
people_cnt = int(input())

for _ in range(people_cnt):
    print(switches)
    sex, switch_num = map(int, input().split())
    
    if sex == BOY:
        change_switch_num = switch_num
        while change_switch_num <= N:
            switches[change_switch_num] = 0 if switches[change_switch_num] == 1 else 1
            change_switch_num += switch_num
    else:
        before = switch_num-1
        after = switch_num+1
        switches[switch_num] = 0 if switches[switch_num] == 1 else 1
        while before > 0 and after <= N and switches[before] == switches[after]:
            switches[before] = 0 if switches[before] == 1 else 1
            switches[after] = 0 if switches[after] == 1 else 1
            before -=1
            after +=1
for index in range(1, len(switches)):
    print(switches[index], end = " ")
    if index % 20 ==0:
        print()