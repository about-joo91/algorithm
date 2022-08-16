strings = input()
check_how_many = input()
cnt = 0
check_how_many_leng = len(check_how_many)
i = 0 
while i < len(strings) and len(check_how_many) != 0:
    if strings[i:i+check_how_many_leng] == check_how_many:
        cnt+=1
        i += check_how_many_leng
    else:
        i+=1
print(cnt)