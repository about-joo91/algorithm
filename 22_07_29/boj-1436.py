check_num = int(input())
cnt = 0
n = 665
while True:
    if '666' in str(n):
        cnt+=1
    if cnt == check_num:
        break
    n+=1
print(n)