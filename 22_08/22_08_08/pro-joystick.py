def recursive(names,i,n, answer):
    if i == len(names):
        answer.append(n)
        return
    recursive(names, i+1, n+ ord(names[i])- ord('A')+1, answer)
    back = len(names) - i
    recursive(names, i+1, n + ord(names[back])- ord('A') + i+1 , answer)
    recursive(names,i-1, n+ord(names[i-1]) - ord('A') )
def solution(name):
    names = list(name)
    answer =[]
    n = ord(names[0])- ord('A')
    recursive(names,1,n,answer)
    return answer

print(solution("JAZ"))

# 푸는중!