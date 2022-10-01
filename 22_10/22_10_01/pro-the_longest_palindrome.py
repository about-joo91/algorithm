def solution(s):
    answer = 1
    length = len(s)
    check_palindrome = [[False] * length for _ in range(length)]

#   문자열 하나는 팰린드롬이다.
    for i in range(length):
        for j in range(length):
            if i == j:
                check_palindrome[i][j] = True
                
#   문자열 두개 이상일 때는 두 문자가 같은 문자면 팰린드롬임
    for i in range(length):
        for j in range(length):
            if i + 1 == j and s[i] == s[j]:
                check_palindrome[i][j] = True
                answer = 2
#   세개 이상일때는 양 끝이 같은 문자열이고 양 끝 안 쪽의 문자열이 팰린드롬이라면 지금 확인하고 있는 문자열도 팰린드롬이다.
#   따라서 0부터 시작한 start와 start에 2부터 시작한 string의 끝을 서로 비교하여 같고
#   start보다 하나 안쪽이면서 start와 stirng_len을 더한 값보다 하나 작은 그러니까 양쪽 끝 문자들의 안쪽 문자열이 팰린드롬인지 저장해둔 
#   check_palindrome을 확인하여 True라면 이 문자열이 팰린드롬이므로 answer를 증가시킨다.
    for string_len in range(2, length):
        for start in range(length - i):
            if s[start] == s[start+string_len] and check_palindrome[start+1][start+string_len-1]:
                check_palindrome[start][start+string_len] = True
                answer = string_len+1
    return answer