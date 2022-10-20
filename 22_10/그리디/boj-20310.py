S = input()
zero_cnt = S.count("0") // 2
one_cnt = S.count("1") // 2

answer = ""
for string in S:
    # 순회하면서 zero_cnt가 0이 아니고 문자열이 0을 가르킨다면
    # answer에 "0"을 더해주고 zero_cnt에서 1을 빼준다.
    if zero_cnt and string == "0":
        answer += string
        zero_cnt -=1
    # 최대한 작은 숫자가 되기 위해서는 1이 최대한 나중에 나와야 한다.
    # 따라서 처음 1의 갯수의 반을 삭제해준다.(answer에 넣지 않는다.)
    if one_cnt and string == "1":
        one_cnt -=1
        continue
    # one_cnt가 0이라면 반은 사라졌기 때문에 나머지 값들을 answer에 더해준다.
    elif string == "1":
        answer += string
print(answer)