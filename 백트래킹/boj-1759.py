len_of_password, cnt_of_alphabets = map(int, input().split())

alphabets = sorted(input().split())

vowels = ["a", "e", "i", "o", "u"]

# 길이가 주어진 len_of_password와 같고
# 최소한 모음을 하나 자음을 두개 가져야하기 때문에 모음이 있는지 검사하고
# 그 갯수를 answer의 길이에서 빼서 그 길이가 2이상이라면 조건이 맞으므로
# True를 리턴한다.
def is_right_condition(len_of_password, answer):
    if len(answer) == len_of_password:
        cnt = 0
        for vowel in vowels:
            if vowel in answer:
                cnt+=1
        if cnt > 0 and len(answer) - cnt > 1:
            return True
    return False

# 가능한 모든 패스워드를 찾는다. 백트래킹을 활용하여 
# 조건에 부합하는 것들을 하나하나 answer에 넣어가면서 확인하고
# 조건에 부합하지 않는 것들은 무시해준다.
def get_possible_password(len_of_password,answer,alphabets):
    
    if is_right_condition(len_of_password, answer):
        print("".join(answer))
        return
    
    for alphabet in alphabets:
        if alphabet not in answer:
            if answer and answer[-1] > alphabet:
                continue
            else:
                answer.append(alphabet)
                get_possible_password(len_of_password, answer, alphabets)
                answer.pop()
            
get_possible_password(len_of_password, [], alphabets)